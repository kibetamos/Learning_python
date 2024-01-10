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


