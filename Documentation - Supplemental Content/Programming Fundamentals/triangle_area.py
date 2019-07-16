import math

def T_area(base, height):
        '''(number, number) -> number

        Return the area of a triangle with dimensions base and height.
        '''
        
        return base * height / 2
def perimeter(side1, side2, side3):
        '''(number, number, number) -> number

        Return the perimeter of a triangle with the sum of its sides.
        '''

        return side1 + side2 + side3

def semiperimeter(side1, side2, side3):
        '''
        (number, number, number) -> float

        Return the semiperimeter of a triangle with sides of side1, side2 and side3.

        >>> semiperimeter(3, 4, 5)
        6.0
        >>> semiperimeter(10.5, 6, 9.3)
        12.9
        '''
        return perimeter(side1, side2, side3) / 2
def area_hero(side1, side2, side3):
        ''' (number, number, number) -> float

        Return the area of a triangle with sides of lenght
        side1, side2 and side3.

        >>> area_hero(3, 4, 5)
        6.0
        >>> area_hero(10.5, 6, 9.3
        27.73168584850189
        '''

        semi = semiperimeter(side1, side2, side3)
        area = math.sqrt(semi * (semi - side1) * (semi - side2) * (semi - side3))
        return area      
semiperimeter(1, 3, 7)
