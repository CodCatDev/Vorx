class Vector2:
    x: float
    y: float

    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        """
        Initializes a new Vector2 instance.
        
        Args:
            x (float): The x-coordinate (default 0.0).
            y (float): The y-coordinate (default 0.0).
        """
        ...
    def __add__(self, other: 'Vector2') -> 'Vector2': ...
    def __sub__(self, other: 'Vector2') -> 'Vector2': ...
    def __mul__(self, scalar: float) -> 'Vector2': ...
    def __truediv__(self, scalar: float) -> 'Vector2': ...
    
    def __iadd__(self, other: 'Vector2') -> 'Vector2': ...
    def __isub__(self, other: 'Vector2') -> 'Vector2': ...
    def __imul__(self, scalar: float) -> 'Vector2': ...
    def __itruediv__(self, scalar: float) -> 'Vector2': ...
    
    def __repr__(self) -> str: ...

    def length(self) -> float:
        """
        Calculates the magnitude (length) of the vector.
        
        Returns:
            float: The vector's length.
        """
        ...

    def lengthSquared(self) -> float:
        """
        Calculates the squared magnitude of the vector.
        Faster than length() as it avoids the square root.
        
        Returns:
            float: The squared length.
        """
        ...

    def dot(self, other: 'Vector2') -> float:
        """
        Calculates the dot product with another vector.
        
        Args:
            other (Vector2): The other vector.
            
        Returns:
            float: The dot product result.
        """
        ...

    def distanceTo(self, other: 'Vector2') -> float:
        """
        Calculates the distance between this vector and another.
        
        Args:
            other (Vector2): The target vector.
            
        Returns:
            float: The distance between the two vectors.
        """
        ...

    def distanceSquaredTo(self, other: 'Vector2') -> float:
        """
        Calculates the squared distance between this vector and another.
        
        Args:
            other (Vector2): The target vector.
            
        Returns:
            float: The squared distance.
        """
        ...

    def normalized(self) -> 'Vector2':
        """
        Returns a new vector with a length of 1.0 (unit vector).
        
        Returns:
            Vector2: A new normalized vector.
        """
        ...

    def normalize(self) -> 'Vector2':
        """
        Normalizes the current vector in-place to a length of 1.0.
        
        Returns:
            Vector2: The modified current vector.
        """
        ...

