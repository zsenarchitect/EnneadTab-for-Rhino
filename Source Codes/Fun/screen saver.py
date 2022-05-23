import rhinoscriptsyntax as rs
import random


rs.DeleteObjects(rs.AllObjects())
size = 1000
srf = rs.AddSrfPt([[0,0,0],[size, 0,0], [size, size, 0], [0, size, 0]])
#srf = rs.RebuildSurface(srf, degree=(3,3), pointcount=(10,10))
rs.EnableRedraw(False)
pts = [rs.AddPoint(size * random.random(),size * random.random(),size * random.random()) for i in range(100)]
rs.HideObjects(pts)
rs.HideObject(srf)

for i in range(1000000):
    print "[Frame {}]".format(i)
    rs.Sleep(0.01)
    rs.EnableRedraw(False)
    try:
        rs.DeleteObject(patch)
    except:
        pass
    patch = rs.AddPatch(pts, srf)
    for pt in pts:
        rs.MoveObject(pt, [0,0,100 * (random.random() - 0.5)])
    
    rs.EnableRedraw(True)
#patch = rs.AddPatch(pts, [20,20])