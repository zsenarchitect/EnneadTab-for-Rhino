import rhinoscriptsyntax as rs
import random

def random_scale_1d_H():

    Ids = rs.GetObjects("Select block instances to rotate", filter = 4096, preselect=True)
    if Ids is None: return


    for Id in Ids:
        pt = rs.BlockInstanceInsertPoint(Id)
        z_scale = random.uniform(1.4, 1.7)
        rs.ScaleObject(Id, pt,[1,1,z_scale],False)

if __name__ == "__main__":
    random_scale_1d_H()
