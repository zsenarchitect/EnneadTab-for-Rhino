import scriptcontext as sc

mats = sc.doc.Materials
mat_names = []
doc_name = sc.doc.Name.split(".3dm")[0]
print doc_name
print mats
print "*******"
for mat in mats:
    try:
        if mat.Name not in mat_names:
            if doc_name in mat.Name:
                continue
            old_name =  mat.Name
            mat.Name = doc_name + "_" + old_name
            print "{} --> {}".format(old_name, mat.Name)
            mat.CommitChanges()
            mat_names.append(mat.Name)
    except:
        continue