
import System
import Rhino
import Rhino.UI
import rhinoscriptsyntax as rs

import Eto
import Eto.Drawing as drawing
import Eto.Forms as forms

import scriptcontext as sc

import os
import fnmatch

import itertools
flatten = itertools.chain.from_iterable
graft = itertools.combinations

# make modal dialog
class DocLayerSelectionDialog(Eto.Forms.Dialog[bool]):
    # Initializer
    def __init__(self, options, title, message,  muti_select, button_names , width, height):
        # Eto initials
        self.Title = title
        self.Resizable = True
        self.Padding = Eto.Drawing.Padding(5)
        self.Spacing = Eto.Drawing.Size(5, 5)
        self.Icon = Eto.Drawing.Icon(r"L:\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\Source Codes\lib\ennead-e-logo.png")
        #self.Bounds = Eto.Drawing.Rectangle()
        self.height = height
        self.width = width
        self.Muti_Select = muti_select
        self.Message = message
        self.Button_Names = button_names


        # fields
        #self.ScriptList = self.InitializeScriptList()
        self.ScriptList = options
        self.SearchedScriptList = self.ScriptList[::]


        # initialize layout
        layout = Eto.Forms.DynamicLayout()
        layout.Padding = Eto.Drawing.Padding(5)
        layout.Spacing = Eto.Drawing.Size(5, 5)


        # add message
        layout.BeginVertical()
        layout.AddRow(self.CreateMessageBar())
        layout.EndVertical()

        # add search
        layout.BeginVertical()
        layout.AddRow(*self.CreateSearchBar())
        layout.EndVertical()

        # add listBox
        layout.BeginVertical()
        layout.AddRow(self.CreateScriptListBox())
        layout.EndVertical()

        # add buttons
        layout.BeginVertical()
        layout.AddRow(*self.CreateButtons())
        layout.EndVertical()

        # set content
        self.Content = layout



    # collect data for list
    def InitializeScriptList(self):
        return allDocLayers
        #return sorted(allDocLayers)

    # create message bar function
    def CreateMessageBar(self):
        self.msg = Eto.Forms.Label()
        self.msg.Text = self.Message
        return self.msg
        #self.msg.HorizontalAlignment = Eto.Forms.HorizontalAlignment.Left

    # create search bar function
    def CreateSearchBar(self):
        """
        Creates two controls for the search bar
        self.lbl_Search as a simple label
        self.tB_Search as a textBox to input search strings to
        """
        self.lbl_Search = Eto.Forms.Label()
        self.lbl_Search.Text = "Search: "
        self.lbl_Search.VerticalAlignment = Eto.Forms.VerticalAlignment.Center

        self.tB_Search = Eto.Forms.TextBox()
        self.tB_Search.TextChanged += self.tB_Search_TextChanged

        return [self.lbl_Search, self.tB_Search]



    def CreateScriptListBox(self):
        # Create a multi selection box with grid view - this is similar to Rhino MultipleListBox
        self.lb = forms.GridView()
        self.lb.ShowHeader = True
        self.lb.AllowMultipleSelection = self.Muti_Select
        self.lb.Height = self.height
        self.lb.AllowColumnReordering = True

        self.lb.DataStore = sorted(self.ScriptList)

        self.lb.SelectedRowsChanged += self.RowsChanged


        # Create Gridview Column
        column1 = forms.GridColumn()
        column1.Editable = False
        column1.Width = self.width
        column1.DataCell = forms.TextBoxCell(0)
        self.lb.Columns.Add(column1)

        self.lb.DataStore = self.SearchedScriptList

        return self.lb



    def CreateButtons(self):
        """
        Creates buttons for either print the selection result
        or exiting the dialog
        """
        user_buttons = []
        for b_name in self.Button_Names:
            self.btn_Run = Eto.Forms.Button()
            self.btn_Run.Text = b_name
            self.btn_Run.Click += self.btn_Run_Clicked
            user_buttons.append(self.btn_Run)

        self.btn_Cancel = Eto.Forms.Button()
        self.btn_Cancel.Text = "Cancel"
        self.btn_Cancel.Click += self.btn_Cancel_Clicked

        user_buttons.extend([ None, self.btn_Cancel])
        return user_buttons



    # create a search function
    def Search(self, text):
        """
        Searches self.ScriptList with a given string
        Supports wildCards
        """
        if text == "":
            self.lb.DataStore = self.ScriptList
        else:
            print self.ScriptList
            temp = [ [str(x[0])] for x in self.ScriptList]
            print temp
            print flatten(temp)
            print fnmatch.filter(flatten(temp), "*" + text + "*")
            print graft(fnmatch.filter(flatten(temp), "*" + text + "*"), 1)
            print list(graft(fnmatch.filter(flatten(temp), "*" + text + "*"), 1))

            self.SearchedScriptList = list(graft(fnmatch.filter(flatten(temp), "*" + text + "*"), 1))

            #original method only work with pure list of string
            #self.SearchedScriptList = list(graft(fnmatch.filter(flatten(self.ScriptList), "*" + text + "*"), 1))
            self.lb.DataStore = self.SearchedScriptList


    # Gridview SelectedRows Changed Event
    def RowsChanged (self,sender,e):
        return self.lb.SelectedRows



    # function to run when call at button click
    def RunScript(self):
        # return selected items
        return self.lb.SelectedItems



    # event handler handling text input in ther search bar
    def tB_Search_TextChanged(self, sender, e):
        self.Search(self.tB_Search.Text)



    # event handler handling clicking on the 'run' button
    def btn_Run_Clicked(self, sender, e):
        # close window after double click action. Otherwise, run with error
        self.Close(True)
        self.RunScript()


    # event handler handling clicking on the 'cancel' button
    def btn_Cancel_Clicked(self, sender, e):
        self.Close(False)



def ShowDocLayerSelectionDialog(options,
                                title = "EA",
                                message = "",
                                muti_select = False,
                                button_names = ["Run"],
                                width = 300,
                                height = 200):


    # for reason not understood yet, value is not displayed in grid view if not contained by list, must convert list format: [1,2,3,"abc"] ----> [[1],[2],[3],["abd"]]
    formated_list = [[x] for x in options]
    """
    i = 0
    while i < len(docLayers):
        to_do.append(docLayers[i:i+1])
        i += 1
    """

    dlg = DocLayerSelectionDialog(formated_list, title, message, muti_select, button_names, width, height)
    rc = Rhino.UI.EtoExtensions.ShowSemiModal(dlg, Rhino.RhinoDoc.ActiveDoc, Rhino.UI.RhinoEtoApp.MainWindow)

    if (rc):


        OUT = [x[0] for x in dlg.RunScript()]
        OUT.sort()
        #pickedLayers.append(dlg.RunScript())

        print OUT
        return OUT

    else:
        print "Dialog did not run"
        return None

"""
if __name__ == "__main__":
    docLayers = rs.LayerNames()

    to_do = []
    i = 0
    while i < len(docLayers):
        to_do.append(docLayers[i:i+1])
        i += 1
    #ShowDocLayerSelectionDialog(to_do)
    print docLayers
    print to_do
    to_do = [[1],["add"],[3],[4]]
    res = ShowDocLayerSelectionDialog(to_do,
                                    title = "new title",
                                    message = "test message",
                                    muti_select = True,
                                    button_names = ["Test Me", "Or me"],
                                    width = 1000,
                                    height = 200)
    print res
"""
