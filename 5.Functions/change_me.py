#change vale of a parameter

def  main():
    value = 99
    print (f'The value is {value}.')
    change_me(value)
    print(f'Back in main the vaue is {value}.')

#change value
def change_me(arg):
    print('Iam changing the value ')
    arg = 0 
    print(f'Now the value is {arg}.')

#call the main function
    
main()
