# from dataclasses import dataclass
from Ray import Ray as ray
from Vec3 import Vec3 as vec3
from abc import ABC, abstractmethod


# @dataclass
class Hit_Record:
    def __init__(self, t: float = None, p: vec3 = None, normal: vec3 = None):
        self.t = t
        self.p = p
        self.normal = normal


class Hittable(ABC):

    @abstractmethod
    def Hit(self, r: ray, t_min: float, t_max: float, rec: Hit_Record) -> bool:
        pass
