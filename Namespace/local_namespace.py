'''
Function that has a local namespace
'''

def my_function():
    local_var = "This is the global namespace"
    print(local_var)  # Accessing variable from the global namespace

my_function()
'''
when we try to call the function outside the function,
It gives an error
'''



# print(local_var)