# The rectangle module has functions that perform # calculations related to rectangles.

def main():
    length = int(input('Enter length '))
    width = int(input('Enter width '))

    area = get_area(length,width)
    print(area)


def get_area(length,width):

    area = length* width
    return area

    

main()