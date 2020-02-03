# The one thing that all ray tracers have is a ray class, and a computation of what color is seen along a ray.
# Let’s think of a ray as a function p(t)=A+t∗B.
# Here p is a 3D position along a line in 3D. A is the ray origin and B is the ray direction.
# The ray parameter t is a real number .
# Plug in a different t and p(t) moves the point along the ray.

from RayTracerTest.Vec3 import Vec3 as vec3


# The ray class has two vectors, the origin and the direction of the ray
# in the form of P(t) = A + t*B
class Ray:
    A: vec3
    B: vec3

    def __init__(self, origin: vec3, direction: vec3):
        self.A = origin
        self.B = direction

    @property
    def GetOrigin(self):
        return self.A

    @property
    def GetDirection(self):
        return self.B

    def PointAtParameter(self,  t: float):
        return self.A + t*self.B 
