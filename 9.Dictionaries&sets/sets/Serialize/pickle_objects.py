#This programme demonstrates object pickling


import pickle

def main():
    again = 'y' # to control loop repetition

    #open a file for binary writing
    output_file = open('info.dat', 'wb')

    #get data until a user wants to stop

    while again.lower() == 'y':
#Get data about a person and save it.
        save_data(output_file)

        #lets check if the user wants more data
        again = input('Enter more data ? (y/n): ')

    output_file.close()
#save function gets data about a person
    # stores it in a dictionary
    #

def save_data(file):
    #create an empty dictionary
    person = {}
    #get data and store

    person['name'] = input('Name: ')
    person['age'] = int(input('Age: '))
    person['weight'] = float(input('Weight: '))

    
    #create an empty dictionary
    pickle.dump(person, file)

    
# Call the main function.
if __name__ == '_ _main_ _':
    main()      