# from dataclasses import dataclass
from RayTracerTest.Ray import Ray as ray
from RayTracerTest.Vec3 import Vec3 as vec3
from abc import ABC, abstractmethod
from typing import List


class Hit_Record:
    def __init__(self, t: float = None, p: vec3 = None, normal: vec3 = None):
        self.t = t
        self.p = p
        self.normal = normal


class Hittable(ABC):
    @abstractmethod
    def Hit(self, r: ray, t_min: float, t_max: float, rec: List[Hit_Record]):
        pass
