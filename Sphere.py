from Hittable import Hittable as hittable
from Vec3 import Vec3 as vec3
from Ray import Ray as ray
from Hittable import Hit_Record as Hit_Record
import math


# noinspection PyMethodParameters
class Sphere(hittable):

    def __init__(self, cen: vec3, r: float):
        self.center: vec3 = cen
        self.radius: float = r

    def Hit(self, r: ray, t_min: float, t_max: float, rec: Hit_Record):
        """

        :rtype: bool
        """
        oc: vec3 = r.GetOrigin - self.center
        a: float = vec3.DotProduct(r.GetDirection, r.GetDirection)
        b: float = 2.0 * vec3.DotProduct(oc, r.GetDirection)
        c: float = vec3.DotProduct(oc, oc) - self.radius * self.radius
        discriminant: float = b * b - 4 * a * c

        if discriminant > 0:
            temp: float = (-b - math.sqrt(discriminant)) / a
            if t_max > temp > t_min:  # COULD GIVE US TROUBLE HERE
                rec.t = temp
                rec.p = r.PointAtParameter(rec.t)
                rec.normal = (rec.p - self.center) / self.radius
                return True
            temp = (-b + math.sqrt(discriminant)) / a
            if t_max > temp > t_min:
                rec.t = temp
                rec.p = r.PointAtParameter(rec.t)
                rec.normal = (rec.p - self.center) / self.radius
                return True

        return False
