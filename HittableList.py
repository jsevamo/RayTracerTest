from RayTracerTest.Hittable import *


# This HittableList class actually helps us build a world of hittable objects.
class HittableList(Hittable):
    # We define an objectList, so we can add hittable objects to this list and make a world.
    def __init__(self, objectList: Hittable = None):
        if objectList is None:
            objectList = []
        self.objectList = objectList

    # Just an append function to add hittable objects to the object list.
    def append(self, objectToAdd: Hittable):
        self.objectList.append(objectToAdd)

    # Now the hit function here will actually check if we hit anything from the world.
    def Hit(self, r: ray, t_min: float, t_max: float, rec: [Hit_Record]) -> bool:
        # If we don't hit anything, this will always be false.
        hitAnything = False
        # Object to type HitRecord to pass to HittableObject to record its hit data.
        tempRec = [Hit_Record()]
        # We want to see with t is the closet hit so far. We start then by assigning the furthest possible value: t_max
        closestSoFar = t_max
        # Running through the object list if it has objects
        if len(self.objectList) > 0:
            for hittableObject in self.objectList:
                # If we hit an object (sphere) we pass the neccesary data to record.
                if hittableObject.Hit(r, t_min, closestSoFar, tempRec):
                    hitAnything = True
                    # Now the closest object is this.
                    closestSoFar = tempRec[0].t
                    rec[0] = tempRec[0]

            return hitAnything
        else:
            print("Nothing in the world")
            return hitAnything
