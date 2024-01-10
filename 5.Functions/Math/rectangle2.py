#Function area accepts width and lenght as parameters

def area(width, length):
    return width *length


#function perimeter takes in wifht and lenght and returns perimetrt

def perimeter(width, length):
    return 2 * (width + length)

#main function is used to test the other functions

def main():
    width = float(input("Enter the rectangle's width: "))
    length = float(input("Enter the rectangle's length: "))
    print('The area is', area(width, length))
    print('The perimeter is', perimeter(width, length))


# Call the main function ONLY if the file is being run as
# a standalone program.
if __name__ == '__main__':
    main()
