'''
We have defined a function inside a function
outer function -  the main function
inner function - function inside a function
'''
def outer_function():
    outer_var = "This is the outer function"

    def inner_function():
        # Accessing variable from the enclosing namespace
        print(outer_var)  
    #call the function
    inner_function()
#call the outer function
outer_function()
'''
Trying to access outer_var outside the function, 
will raise a NameError
print(outer_var)
'''
print(outer_var)