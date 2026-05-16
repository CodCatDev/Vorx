from libc.stdlib cimport malloc, free
from libc.stdint cimport uintptr_t

cdef extern from "SDL.h":
    cdef struct SDL_Renderer:
        pass
        
    cdef struct SDL_FPoint:
        float x
        float y
        
    cdef struct SDL_Color:
        unsigned char r
        unsigned char g
        unsigned char b
        unsigned char a
        
    cdef struct SDL_Vertex:
        SDL_FPoint position
        SDL_Color color
        SDL_FPoint tex_coord
        
    int SDL_RenderGeometry(SDL_Renderer* renderer, void* texture, 
                           SDL_Vertex* vertices, int num_vertices, 
                           int* indices, int num_indices)

from vorx.objects.shapes cimport Shape, Rect, Polygon, ShapeType, SHAPE_RECT, SHAPE_POLYGON

DEF MAX_VERTICES = 10000
DEF MAX_INDICES = 30000

cdef SDL_Vertex batch_vertices[MAX_VERTICES]
cdef int batch_indices[MAX_INDICES]

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
        v_arr[v + idx].tex_coord.x = 0.0
        v_arr[v + idx].tex_coord.y = 0.0

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
        v_arr[v + idx].tex_coord.x = 0.0
        v_arr[v + idx].tex_coord.y = 0.0

    for idx in range(num_pts - 2):
        i_arr[i] = v
        i_arr[i+1] = v + idx + 1
        i_arr[i+2] = v + idx + 2
        i += 3

    v_off[0] += num_pts
    i_off[0] += i

cpdef void renderScene(size_t rendererAddr, list shapes):
    cdef SDL_Renderer* renderer = <SDL_Renderer*>rendererAddr
    cdef int v_offset = 0
    cdef int i_offset = 0
    cdef Shape base_shape

    for obj in shapes:
        base_shape = <Shape>obj
        
        if v_offset + 100 > MAX_VERTICES or i_offset + 300 > MAX_INDICES:
            SDL_RenderGeometry(renderer, NULL, batch_vertices, v_offset, batch_indices, i_offset)
            v_offset = 0
            i_offset = 0
            
        if base_shape.type == SHAPE_RECT:
            pushRect(batch_vertices, batch_indices, &v_offset, &i_offset, <Rect>obj)
        elif base_shape.type == SHAPE_POLYGON:
            pushPolygon(batch_vertices, batch_indices, &v_offset, &i_offset, <Polygon>obj)

    if v_offset > 0:
        SDL_RenderGeometry(renderer, NULL, batch_vertices, v_offset, batch_indices, i_offset)