# Tuple representing coordinates (x, y)
point1 = (3, 5)
point2 = (-1, 2)
point3 = (0, 0)

# Accessing elements
print("Coordinates of point1:", point1)  # Output: (3, 5)
print("X-coordinate of point2:", point2[0])  # Output: -1
print("Y-coordinate of point3:", point3[1])  # Output: 0

# Tuple unpacking for clarity
x, y = point1
print("X-coordinate of point1:", x)  # Output: 3
print("Y-coordinate of point1:", y)  # Output: 5

# Concatenating tuples
combined_point = point1 + point2
print("Combined coordinates:", combined_point)  # Output: (3, 5, -1, 2)

# Length of a tuple
num_elements = len(point3)
print("Number of elements in point3:", num_elements)  # Output: 2
