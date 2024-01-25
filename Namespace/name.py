global_var = "I'm in the global namespace"

def my_function():
    print(global_var)  # Accessing variable from the global namespace

my_function()
print(global_var)