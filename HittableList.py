from RayTracerTest.Hittable import *


class HittableList(Hittable):

    def __init__(self, objectList: [Hittable] = None):
        if objectList is None:
            objectList = []
        self.objectList = objectList

    def append(self, objectToAdd: Hittable):
        self.objectList.append(objectToAdd)

    def Hit(self, r: ray, t_min: float, t_max: float, rec: [Hit_Record]) -> bool:
        hitAnything = False
        tempRec = [Hit_Record()]
        closestSoFar = t_max

        for hittableObject in self.objectList:
            if hittableObject.Hit(r, t_min, closestSoFar, tempRec):
                hitAnything = True
                closestSoFar = tempRec[0].t
                rec[0] = tempRec[0]

        return hitAnything
