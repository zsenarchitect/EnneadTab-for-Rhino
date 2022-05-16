import rhinoscriptsyntax as rs
import random

def random_block():

    Ids = rs.GetObjects("Select block instances to rotate", filter = 4096, preselect=True)
    if Ids is None: return
    vec = rs.VectorCreate([0,0,1], [0,0,0])


    for Id in Ids:
        pt = rs.BlockInstanceInsertPoint(Id)
        ang = random.randrange(-180, 180)
        rs.RotateObject(Id, pt,ang,vec)

        z_scale = random.uniform(0.9, 1.1)
        rs.ScaleObject(Id, pt,[1,1,z_scale],False)

if __name__ == "__main__":
    random_block()
