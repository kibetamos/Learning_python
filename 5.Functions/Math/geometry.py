import rectangle

import circle

#constants 

area_circle = 1
circumference_choice = 2
area_rectangle_choice = 3
perimeter_rectanle_choice = 4
quit_choice = 5

#main function
def main():
    #controls the loop and holds users menu ChildProcessError
    choice = 0

    while choice != quit_choice:
        #display menu'
        display_menu()

        #get the users choice

        choice =  int(input('Enter your choice '))

        #basing on the choice selected lets dislay the menu
        if choice == circumference_choice:
            radius = float(input("Enter the circle's radius : "))
            print('The circumference is ', circle.circumference(radius))

        elif choice == area_circle:
            radius = float(input('Enter circles radius :'))

            print('The area is ', circle.area(radius))
        
        elif choice == area_rectangle_choice:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print('The area is', rectangle.area(width, length))

        elif choice == perimeter_rectanle_choice:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))

            print('The perimeter is', rectangle.perimeter(width, length))


        elif choice == quit_choice:

            print('Exiting the program. . .')

        else:

            print('Error: invalid selection.')


