cimport cython
from libc.math cimport sqrtf

cdef struct Vec2:
    float x
    float y

cdef inline Vec2 vec2Add(Vec2 a, Vec2 b) noexcept nogil:
    return Vec2(a.x + b.x, a.y + b.y)

cdef inline Vec2 vec2Sub(Vec2 a, Vec2 b) noexcept nogil:
    return Vec2(a.x - b.x, a.y - b.y)

cdef inline Vec2 vec2Mul(Vec2 a, float s) noexcept nogil:
    return Vec2(a.x * s, a.y * s)

cdef inline Vec2 vec2Div(Vec2 a, float s) noexcept nogil:
    return Vec2(a.x / s, a.y / s)

cdef inline float vec2Len(Vec2 a) noexcept nogil:
    return sqrtf(a.x * a.x + a.y * a.y)

cdef inline float vec2LenSq(Vec2 a) noexcept nogil:
    return a.x * a.x + a.y * a.y

cdef inline float vec2Dot(Vec2 a, Vec2 b) noexcept nogil:
    return a.x * b.x + a.y * b.y

cdef inline float vec2Dist(Vec2 a, Vec2 b) noexcept nogil:
    cdef float dx = a.x - b.x
    cdef float dy = a.y - b.y
    return sqrtf(dx * dx + dy * dy)

cdef inline float vec2DistSq(Vec2 a, Vec2 b) noexcept nogil:
    cdef float dx = a.x - b.x
    cdef float dy = a.y - b.y
    return dx * dx + dy * dy

cdef inline Vec2 vec2Norm(Vec2 a) noexcept nogil:
    cdef float l = sqrtf(a.x * a.x + a.y * a.y)
    if l == 0:
        return Vec2(0.0, 0.0)
    return Vec2(a.x / l, a.y / l)

@cython.freelist(10000)
cdef class Vector2:
    cdef public float x, y

    def __cinit__(self, float x=0.0, float y=0.0):
        self.x = x
        self.y = y

    cdef inline Vec2 asVec2(self) nogil:
        return Vec2(self.x, self.y)

    def __add__(Vector2 self, Vector2 other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(Vector2 self, Vector2 other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(Vector2 self, float s):
        return Vector2(self.x * s, self.y * s)

    def __truediv__(Vector2 self, float s):
        if s == 0:
            raise ZeroDivisionError()
        return Vector2(self.x / s, self.y / s)
    
    def __iadd__(self, Vector2 other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, Vector2 other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __imul__(self, float s):
        self.x *= s
        self.y *= s
        return self

    def __itruediv__(self, float s):
        if s == 0:
            raise ZeroDivisionError()
        self.x /= s
        self.y /= s
        return self


    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"

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
