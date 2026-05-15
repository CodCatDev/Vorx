cdef class Shape:
    pass

cdef class Rect(Shape):
    def __init__(self, float x, float y, float w, float h, unsigned char r, unsigned char g, unsigned char b):
        self.type = SHAPE_RECT
        self.x, self.y, self.w, self.h = x, y, w, h
        self.r, self.g, self.b = r, g, b

cdef class Polygon(Shape):
    def __init__(self, list points, unsigned char r, unsigned char g, unsigned char b):
        self.type = SHAPE_POLYGON
        self.points = points
        self.r, self.g, self.b = r, g, b
