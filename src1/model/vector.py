import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        return self

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def limit(self, max_magnitude):
        magnitude = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        if magnitude > max_magnitude:
            scale_factor = max_magnitude / magnitude
            self.x *= scale_factor
            self.y *= scale_factor
            self.z *= scale_factor