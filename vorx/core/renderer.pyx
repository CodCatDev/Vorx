from libc.stdlib cimport malloc, free
from libc.stdint cimport uintptr_t

from vorx.objects.shapes cimport Shape, Rect, Polygon, ShapeType, SHAPE_RECT, SHAPE_POLYGON

cdef struct SDL_Color:
    unsigned char r, g, b, a
cdef struct SDL_FPoint:
    float x, y
cdef struct SDL_Vertex:
    SDL_FPoint position
    SDL_Color color
    SDL_FPoint tex_coord

cdef inline void pushRect(SDL_Vertex* v_arr, int* i_arr, int* v_off, int* i_off, Rect obj):
    cdef int v = v_off[0]
    cdef int i = i_off[0]
    cdef float x = obj.x, y = obj.y, w = obj.w, h = obj.h
    cdef unsigned char r = obj.r, g = obj.g, b = obj.b

    v_arr[v].position.x = x;       v_arr[v].position.y = y
    v_arr[v+1].position.x = x + w; v_arr[v+1].position.y = y
    v_arr[v+2].position.x = x + w; v_arr[v+2].position.y = y + h
    v_arr[v+3].position.x = x;     v_arr[v+3].position.y = y + h

    cdef int idx
    for idx in range(4):
        v_arr[v + idx].color.r = r
        v_arr[v + idx].color.g = g
        v_arr[v + idx].color.b = b
        v_arr[v + idx].color.a = 255

    i_arr[i] = v; i_arr[i+1] = v+1; i_arr[i+2] = v+2
    i_arr[i+3] = v+2; i_arr[i+4] = v+3; i_arr[i+5] = v

    v_off[0] += 4
    i_off[0] += 6

cdef inline void pushPolygon(SDL_Vertex* v_arr, int* i_arr, int* v_off, int* i_off, Polygon obj):
    cdef int v = v_off[0]
    cdef int i = i_off[0]
    cdef int num_pts = <int>len(obj.points)
    cdef unsigned char r = obj.r, g = obj.g, b = obj.b
    cdef float px, py
    cdef int idx

    for idx in range(num_pts):
        px, py = obj.points[idx]
        v_arr[v + idx].position.x = px
        v_arr[v + idx].position.y = py
        v_arr[v + idx].color.r = r
        v_arr[v + idx].color.g = g
        v_arr[v + idx].color.b = b
        v_arr[v + idx].color.a = 255

    for idx in range(num_pts - 2):
        i_arr[i] = v
        i_arr[i+1] = v + idx + 1
        i_arr[i+2] = v + idx + 2
        i += 3

    v_off[0] += num_pts
    i_off[0] += (num_pts - 2) * 3

cpdef tuple buildGeometryBatch(list shapes):
    cdef int total_v = 0
    cdef int total_i = 0
    cdef Shape base_shape

    for obj in shapes:
        base_shape = <Shape>obj
        if base_shape.type == SHAPE_RECT:
            total_v += 4
            total_i += 6
        elif base_shape.type == SHAPE_POLYGON:
            total_v += <int>len((<Polygon>obj).points)
            total_i += <int>(len((<Polygon>obj).points) - 2) * 3

    if total_v == 0:
        return (0, 0, 0, 0)

    cdef SDL_Vertex* vertices = <SDL_Vertex*>malloc(total_v * sizeof(SDL_Vertex))
    cdef int* indices = <int*>malloc(total_i * sizeof(int))

    cdef int v_offset = 0
    cdef int i_offset = 0

    for obj in shapes:
        base_shape = <Shape>obj
        if base_shape.type == SHAPE_RECT:
            pushRect(vertices, indices, &v_offset, &i_offset, <Rect>obj)
        elif base_shape.type == SHAPE_POLYGON:
            pushPolygon(vertices, indices, &v_offset, &i_offset, <Polygon>obj)

    return (<size_t>vertices, <size_t>indices, total_v, total_i)

cpdef void freeGeometryBatch(size_t v_addr, size_t i_addr):
    free(<void*>v_addr)
    free(<void*>i_addr)
