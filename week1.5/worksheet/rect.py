# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError()
        elif width <= 0 or height <= 0:
            raise ValueError
        
        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height

    def is_square(self) -> bool:
        """_summary_

        Returns:
            bool: whether or not this is a square by checking if height and width is the same
        """
        return self.height == self.width
    
    def area(self) -> float:
        """_summary_

        Returns:
            float: the area of the rectangle
        """
        return self.height * self.width

    def perimeter(self) -> float:
        """_summary_

        Returns:
            float: the perimeter of the rectangle
        """
        return (self.height + self.width) * 2
    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)

Rectangle(2, 0)