cdef enum ShapeType:
    SHAPE_RECT
    SHAPE_POLYGON

cdef class Shape:
    cdef public ShapeType type
    cdef public unsigned char r, g, b

cdef class Rect(Shape):
    cdef public float x, y, w, h

cdef class Polygon(Shape):
    cdef public list points
