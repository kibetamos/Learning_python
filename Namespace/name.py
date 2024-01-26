global_var = "This is the global namespace"

def my_function():
    print(global_var)  # Accessing variable from the global namespace

my_function()
print(global_var)