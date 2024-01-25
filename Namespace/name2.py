# Using a built-in function and object
# print(len([1, 2, 3]))

# Trying to redefine a built-in function
# This will raise a SyntaxError
def len(x):
    return 42

# Test the custom len function
my_list = [1, 2, 3, 4, 5]
result = len(my_list)

# Display the result on the terminal
print(result)


print(len([1, 2, 3]))