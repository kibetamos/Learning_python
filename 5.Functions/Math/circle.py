import math
def main():
    radius = float(input('Enter the radius'))

    area = calculate_area(radius)

    print(area)

def calculate_area(radius):
    
    area = math.pi *radius**2
    return area

main()