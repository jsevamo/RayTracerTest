# from dataclasses import dataclass
from RayTracerTest.Ray import Ray as ray
from RayTracerTest.Vec3 import Vec3 as vec3


# @dataclass
class Hit_Record:
    t: float
    p: vec3
    normal: vec3


# noinspection PyMethodParameters
class Hittable:

    def Hit(self, r: ray, t_min: float, t_max: float, rec: Hit_Record):
        pass

