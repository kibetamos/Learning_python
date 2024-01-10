# The rectangle module has functions that perform # calculations related to rectangles.
import math
# def main():

#     width = float(input("Enter the rectangle's width: "))
#     length = float(input("Enter the rectangle's length: "))

#     area = get_area(length,width)
#     perimeter = get_perimeter(length,width)

#     print('The area is,', area)
#     print('The perimeter is,', perimeter)

# def get_area(length,width):

#     area = length* width
#     return area


# def get_perimeter(length, width):
#     perimeter = 2 * (width + length)

#     return perimeter

# main()

def area(width,length):
    return width*length

def perimeter(width, lenght):
    return 2 * (width + lenght)

def main():
    width = float(input("Enter the rectangle's width: "))
    length = float(input("Enter the rectangle's length: "))
    print('The area is', area(width, length))
    print('The perimeter is', perimeter(width, length))


main()