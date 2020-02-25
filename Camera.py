import random
from RayTracerTest.Vec3 import Vec3 as vec3
from RayTracerTest.Ray import Ray as ray


class RandomH:
    def __init__(self):
        pass

    def RandomFloat(self) -> float:
        return random.uniform(0, 1)


class Camera:
    def __init__(self):
        self.lowerLeftCorner: vec3 = vec3(-2.0, -1.0, -1.0)
        self.horizontalSize: vec3 = vec3(4.0, 0.0, 0.0)
        self.verticalSize: vec3 = vec3(0.0, 2.0, 0.0)
        self.originOfCamera: vec3 = vec3(0.0, 0.0, 0.0)

    def GetRay(self, u: float, v: float) -> ray:
        return ray(self.originOfCamera, self.lowerLeftCorner + u * self.horizontalSize + v * self.verticalSize - self.originOfCamera)
