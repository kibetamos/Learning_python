# lets programm demonstarte passing two strings arguments to a function

def main():
    firstname = input('Enter your firstname')
    lastname = input('Enter your lastname')

    print('Your name reversed is')
    
    reverse_name(firstname, lastname)

def reverse_name(first, last):
    print(last, first)

main()
