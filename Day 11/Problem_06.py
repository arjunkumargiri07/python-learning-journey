class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __str__(self):
        return f"Vector({self.x}i + {self.y}j + {self.z}k)"

v1 = Vector(2, 3, 4)
v2 = Vector(5, 6, 7)
v3 = Vector(1, 2, 3)

print(v1 + v2)  # Output: Vector(7, 9, 11)
print(v1 - v2)  # Output: Vector(-3, -3, -3)
print(v1 * 2)   # Output: Vector(4, 6, 8)
print(v1)       # Output: Vector(2i + 3j + 4k)
