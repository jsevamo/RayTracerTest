# from dataclasses import dataclass
from RayTracerTest.Ray import Ray as ray
from RayTracerTest.Vec3 import Vec3 as vec3
from abc import ABC, abstractmethod


# This file is very important. It contains two classes: Hit_Record and Hittable. Hit_Record is used as an struct to
# store hit data.
# Hittable is an abstract class (and method) used in other classes to implement what happens when you hit an object.


# Everytime the ray hits something we want to store the t value when it hit, the point p where it hit (3D vector) and
# the normal vector at that point p. We use this class for that purpose.
class Hit_Record:
    def __init__(self, t: float = None, p: vec3 = None, normal: vec3 = None):
        self.t = t
        self.p = p
        self.normal = normal


# And then we make the Hittable class, that has a method called Hit(). Hit asks for:
# 1. a ray.
# 2. t_min and t_max because we want to implement a t interval for rendering.
# 3. A list of objects type Hit_Record so we can have a list of Hits. Each of these hits stores values of t, p, and normal.
class Hittable(ABC):
    @abstractmethod
    def Hit(self, r: ray, t_min: float, t_max: float, rec: [Hit_Record]):
        pass
