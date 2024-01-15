# Difference between Lists and Tuples
    Tuples and lists are both data structures in Python, but they have some key differences:
## Mutability:
    Lists: Lists are mutable, meaning you can modify their elements after creation. You can add, remove, or change items in a list
    Tuples: Tuples are immutable. Once a tuple is created, you cannot change, add, or remove elements. This immutability can provide certain advantages in terms of data integrity and safety.

## Syntax:
    Lists: Defined using square brackets [].
    Tuples: Defined using parentheses ().

## Use Cases:
    Lists: Use lists when you need a collection of items that may need to be modified, such as adding or removing elements. Lists are suitable for situations where the order of elements matters, and you need dynamic data structures.
    Tuples: Use tuples when you want an immutable, ordered collection of items. Tuples are often used when the data should remain constant throughout the program, such as representing coordinates, settings, or other fixed sets of values.

## Methods:
    Lists: Have more built-in methods for modification, such as append(), extend(), insert(), remove(), and pop().
    Tuples: Have fewer methods due to their immutability, mainly providing methods for basic operations like count() and index().