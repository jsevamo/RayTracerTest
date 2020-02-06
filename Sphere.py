from RayTracerTest.Hittable import Hittable as hittable
from RayTracerTest.Vec3 import Vec3 as vec3
from RayTracerTest.Ray import Ray as ray
from RayTracerTest.Hittable import Hit_Record as Hit_Record


# noinspection PyMethodParameters
class Sphere(hittable):

    def __init__(self, cen: vec3, r: float):
        self.center: vec3 = cen
        self.radius: float = r

    def Hit(self, r: ray, t_min: float, t_max: float, rec: Hit_Record):
        oc: vec3 = r.GetOrigin - self.center
        a: float = vec3.DotProduct(r.GetDirection, r.GetDirection)
        b: float = 2.0 * vec3.DotProduct(oc, r.GetDirection)
        c: float = vec3.DotProduct(oc, oc) - self.radius * self.radius
        discriminant: float = b * b - 4 * a * c