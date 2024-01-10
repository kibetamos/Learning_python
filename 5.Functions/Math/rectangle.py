# The rectangle module has functions that perform # calculations related to rectangles.

def main():

    width = float(input("Enter the rectangle's width: "))
    length = float(input("Enter the rectangle's length: "))

    area = get_area(length,width)
    perimeter = get_perimeter(length,width)

    print('The area is,', area)
    print('The perimeter is,', perimeter)

def get_area(length,width):

    area = length* width
    return area


def get_perimeter(length, width):
    perimeter = 2 * (width + length)

    return perimeter

main()