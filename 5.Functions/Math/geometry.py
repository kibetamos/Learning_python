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

        if choice == area_circle:
            radius = float(input('Enter circles radius :'))

            print('The area is ', circle.area(radius))
        
        #basing on the choice selected lets dislay the menu
        elif choice == circumference_choice:
            radius = float(input("Enter the circle's radius : "))
            print('The circumference is ', circle.circumference(radius))


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


# The display_menu function displays a menu.
def display_menu():
    
    print(' MENU')
    print('1) Area of a circle')
    print('2) Circumference of a circle')
    print('3) Area of a rectangle')
    print('4) Perimeter of a rectangle')
    print('5) Quit')

 # Call the main function.
main()