from libc.math cimport sqrt

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

    def length(self):
        return sqrt(self.x * self.x + self.y * self.y)

    def normalized(self):
        cdef float l = sqrt(self.x * self.x + self.y * self.y)
        if l == 0:
            return Vector2(0.0, 0.0)
        
        # возвращаем новый вектор
        return Vector2(self.x / l, self.y / l)

    def normalize(self):
        # или меняем текущий (in-place)
        cdef float l = sqrt(self.x * self.x + self.y * self.y)
        if l != 0:
            self.x /= l
            self.y /= l