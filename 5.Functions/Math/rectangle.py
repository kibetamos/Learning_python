# The rectangle module has functions that perform # calculations related to rectangles.

def main():
    length = int(input('Enter length '))
    width = int(input('Enter width '))

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