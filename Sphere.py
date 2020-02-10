from RayTracerTest.Hittable import Hittable as hittable
from RayTracerTest.Vec3 import Vec3 as vec3
from RayTracerTest.Ray import Ray as ray
from RayTracerTest.Hittable import *
import math


# Sphere class that handles the rendering of a sphere, and the recording of hits. Came from HitSphere() in Main.

class Sphere(hittable):

    # The Sphere has a center and a radius, so we use that.
    def __init__(self, cen: vec3, r: float):
        self.center: vec3 = cen
        self.radius: float = r

    # Function to check if a ray hit the sphere.
    def Hit(self, r: ray, t_min: float, t_max: float, rec: [Hit_Record]) -> bool:
        # The explanation of this is at HitSphere in Main.
        oc: vec3 = r.GetOrigin - self.center
        a: float = vec3.DotProduct(r.GetDirection, r.GetDirection)
        b: float = 2.0 * vec3.DotProduct(oc, r.GetDirection)
        c: float = vec3.DotProduct(oc, oc) - self.radius * self.radius
        discriminant: float = (b * b) - (4 * a * c)

        # If the discriminat is more than 0, mean we hit the sphere.
        if discriminant > 0:
            # We check for hits with smallest t (closets to screen) by using - after -b.
            # temp is just the value of t where we hit the sphere.
            temp = (-b - math.sqrt(discriminant)) / (a * 2.0)
            # if temp is between our t_min and t_max, we record a hit with RecordHit()
            # and return true to indicate we did hit.
            if t_min < temp < t_max:
                self.RecordHit(temp, r, rec)
                return True
            # Same as before but with biggest t value.
            temp = (-b + math.sqrt(discriminant)) / (a * 2.0)
            if t_min < temp < t_max:
                self.RecordHit(temp, r, rec)
                return True
        # If we didn't hit anything, we return false. I mean, I'm trying to explain this the best I can but c'mon
        # this can't be that hard.
        return False

    # This function is called everytime we hit the sphere with a ray. We use this to record the data we need with each
    # hit. Like we said at Hittable, we record t, p and the normal vector.
    def RecordHit(self, t: float, r: ray, rec: [Hit_Record]):
        rec[0].t = t
        rec[0].p = r.PointAtParameter(rec[0].t)
        rec[0].normal = (rec[0].p - self.center)  # / self.radius
        rec[0].normal.MakeUnitVector()
