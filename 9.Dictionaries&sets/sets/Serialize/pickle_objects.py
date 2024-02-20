#This programme demonstrates object pickling


import pickle

def main():
    again = 'y' # to control loop repetition

    #open a file for binary writing
    output_file = open('info.dat', 'wb')

    #get data until a user wants to stop