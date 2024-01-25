#This programme uses the firstname, lastnameand id number to geneerate
#login name

import login

def main():
    #get the users firstname, lastname and ID
    first = input('Enter your firstname')
    last = input('Enter your last name')

    idnumber = input('Enter your student ID number')

    #get the login name
    print('Your login name is: ')
    print(login.get_login_name(first, last, idnumber))

#call the main function
if __name__ == '__main__':
    main()