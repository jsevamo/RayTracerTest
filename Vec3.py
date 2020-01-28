import math


class Vec3:
    # This are the variables that will hold the 3 numbers for the Vector 3 class.
    q1: float = None
    q2: float = None
    q3: float = None

    # Constructor for the class
    def __init__(self, e0: float, e1: float, e2: float):
        self.q1 = e0
        self.q2 = e1
        self.q3 = e2

    # Returning here X, Y, Z, and R G B value from coordinates[]
    @property
    def x(self):
        return self.q1

    @property
    def y(self):
        return self.q2

    @property
    def z(self):
        return self.q3

    @property
    def r(self):
        return self.q1

    @property
    def g(self):
        return self.q2

    @property
    def b(self):
        return self.q3

    # Getting the length of the vector
    @property
    def Length(self):
        return math.sqrt(self.q1 * self.q1 + self.q2 * self.q2 + self.q3 * self.q3)

    # The squared length of the vector is good to avoid computational costs of the square root
    @property
    def SquaredLength(self):
        return self.q1 * self.q1 + self.q2 * self.q2 + self.q3 * self.q3

    # Turn the vector into a unit vector
    def MakeUnitVector(self):
        k: float = 1.0 / math.sqrt(self.q1 * self.q1 + self.q2 * self.q2 + self.q3 * self.q3)
        self.q1 *= k
        self.q2 *= k
        self.q3 *= k

    # Overloading for printing
    def __str__(self):
        return "(" + str(self.q1) + ", " + str(self.q2) + ", " + str(self.q3) + ")"

    # Overloading for addition, substraction, multiplication (vector and scalar) and division (vector and scalar)
    def __add__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self.q1 + other.q1, self.q2 + other.q2, self.q3 + other.q3)

    def __sub__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self.q1 - other.q1, self.q2 - other.q2, self.q3 - other.q3)

    def __mul__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self.q1 * other.q1, self.q2 * other.q2, self.q3 * other.q3)
        elif isinstance(other, float):
            return Vec3(self.q1 * other, self.q2 * other, self.q3 * other)
        elif isinstance(other, int):
            return Vec3(self.q1 * other, self.q2 * other, self.q3 * other)

    def __truediv__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self.q1 / other.q1, self.q2 / other.q2, self.q3 / other.q3)
        elif isinstance(other, float):
            return Vec3(self.q1 / other, self.q2 / other, self.q3 / other)
        elif isinstance(other, int):
            return Vec3(self.q1 / other, self.q2 / other, self.q3 / other)

    # Dot product
    def DotProduct(v1, v2):
        if isinstance(v1, Vec3):
            if isinstance(v2, Vec3):
                return v1.q1 * v2.q1 + v1.q2 * v2.q2 + v1.q3 * v2.q3

    # Cross product
    def CrossProduct(v1, v2):
        if isinstance(v1, Vec3):
            if isinstance(v2, Vec3):
                return Vec3(v1.q2 * v2.q3 - v1.q3 * v2.q2,
                            v1.q3 * v2.q1 - v1.q1 * v2.q3,
                            v1.q1 * v2.q2 - v1.q2 * v2.q1)
