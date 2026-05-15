from typing import List, Tuple

SHAPE_RECT: int
SHAPE_POLYGON: int

class Shape:
    """
    Base class for shapes
    """
    type: int
    r: int
    g: int
    b: int

class Rect(Shape):
    x: float
    y: float
    w: float
    h: float
    
    def __init__(self, x: float, y: float, w: float, h: float, r: int, g: int, b: int) -> None: 
        """
        A Rectangle shape

        :param x: X coordinate
        :type x: float
        :param y: Y coordinate
        :type y: float
        :param w: Width 
        :type w: float
        :param h: Height
        :type h: float
        :param r: Red (color)
        :type r: int
        :param g: Green (color)
        :type g: int
        :param b: Blue (color)
        :type b: int
        """
        ...

class Polygon(Shape):
    points: List[Tuple[float, float]]
    
    def __init__(self, points: List[Tuple[float, float]], r: int, g: int, b: int) -> None: 
        """
        A Polygon shape.

        :param points: Points of the polygon in format `[(x1, y1), (x2, y2), ...]`
        :type points: List[Tuple[float, float]]
        :param r: Red (color)
        :type r: int
        :param g: Green (color)
        :type g: int
        :param b: Blue (color)
        :type b: int
        """
        ...
