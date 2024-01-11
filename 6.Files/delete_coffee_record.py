#Allows a user delete s record in the coffee tt fie

import os

def main():
    found = False

    #get cofee to delete

    search = input('Which coffee do you want to delete? ')

    #open original coffee.txt file
    coffee_file = open('coffee.txt', 'r')

    #open temporary file
    temp_file = open('temp.txt', 'w')
    
    #Read the first records descrition fiel
    descr = coffee_file.readline()
    
     