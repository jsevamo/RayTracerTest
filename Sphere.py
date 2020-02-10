from RayTracerTest.Hittable import Hittable as hittable
from RayTracerTest.Vec3 import Vec3 as vec3
from RayTracerTest.Ray import Ray as ray
from RayTracerTest.Hittable import *
import math


class Sphere(hittable):

    def __init__(self, cen: vec3, r: float):
        self.center: vec3 = cen
        self.radius: float = r

    def RecordHit(self, t: float, r: ray, rec: List[Hit_Record]):
        rec[0].t = t
        rec[0].p = r.PointAtParameter(rec[0].t)
        rec[0].normal = (rec[0].p - self.center) / self.radius

    def Hit(self, r: ray, t_min: float, t_max: float, rec: List[Hit_Record]) -> bool:
        oc: vec3 = r.GetOrigin - self.center
        a: float = vec3.DotProduct(r.GetDirection, r.GetDirection)
        b: float = 2.0 * vec3.DotProduct(oc, r.GetDirection)
        c: float = vec3.DotProduct(oc, oc) - self.radius * self.radius
        discriminant: float = (b * b) - (4 * a * c)

        if discriminant > 0:
            temp = (-b - math.sqrt(discriminant)) / (a * 2.0)
            if t_min < temp < t_max:
                self.RecordHit(temp, r, rec)
                return True

            temp = (-b + math.sqrt(discriminant)) / (a * 2.0)
            if t_min < temp < t_max:
                self.RecordHit(temp, r, rec)
                return True

        return False
