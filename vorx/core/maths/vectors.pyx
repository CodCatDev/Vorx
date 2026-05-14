from libc.math cimport sqrtf

cdef class Vector2:
    cdef public float x, y

    def __init__(self, float x=0.0, float y=0.0):
        self.x = x
        self.y = y

    def __add__(self, Vector2 other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, Vector2 other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, float scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"

    def __truediv__(self, float scalar):
        if scalar == 0:
            raise ZeroDivisionError("Vector2 division by zero")
        return Vector2(self.x / scalar, self.y / scalar)

    cpdef float length(self):
        return sqrtf(self.x * self.x + self.y * self.y)

    cpdef float lengthSquared(self):
        return self.x * self.x + self.y * self.y

    cpdef float dot(self, Vector2 other):
        return self.x * other.x + self.y * other.y

    cpdef float distanceTo(self, Vector2 other):
        cdef float dx = self.x - other.x
        cdef float dy = self.y - other.y
        return sqrtf(dx * dx + dy * dy)

    cpdef float distanceSquaredTo(self, Vector2 other):
        cdef float dx = self.x - other.x
        cdef float dy = self.y - other.y
        return dx * dx + dy * dy

    cpdef Vector2 normalized(self):
        cdef float l = sqrtf(self.x * self.x + self.y * self.y)
        if l == 0:
            return Vector2(0.0, 0.0)
        
        return Vector2(self.x / l, self.y / l)

    cpdef Vector2 normalize(self):
        cdef float l = sqrtf(self.x * self.x + self.y * self.y)
        if l != 0:
            self.x /= l
            self.y /= l
        
        return self