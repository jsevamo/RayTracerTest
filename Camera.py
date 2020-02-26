import random
from RayTracerTest.Vec3 import Vec3 as vec3
from RayTracerTest.Ray import Ray as ray


# This function is called in Main() in order to shift a bit the direction of the rays.
def RandomFloat() -> float:

    return random.uniform(0, 1)



# The camera class makes things more tidy. The explanation of what is going on here can be found in Main() where
# this code used to be.
# Now has a function that returns a ray given U and V coordinates.
class Camera:
    def __init__(self):
        self.lowerLeftCorner: vec3 = vec3(-2.0, -1.0, -1.0)
        self.horizontalSize: vec3 = vec3(4.0, 0.0, 0.0)
        self.verticalSize: vec3 = vec3(0.0, 2.0, 0.0)
        self.originOfCamera: vec3 = vec3(0.0, 0.0, 0.0)

    def GetRay(self, u: float, v: float) -> ray:
        return ray(self.originOfCamera,
                   self.lowerLeftCorner + self.horizontalSize * u + (self.verticalSize * v) - self.originOfCamera)
