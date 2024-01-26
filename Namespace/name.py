'''
Function that has a glocal namespace
'''
global_var = "This is the global namespace"

def my_function():
     # Accessing variable from the global namespace
    print(global_var) 

my_function()
'''
We can access the global namespace from outside the function

'''
print(global_var)