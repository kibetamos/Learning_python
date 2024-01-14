#Calculates the total of the sum of values in a list

def main():
    books = [50,2,4,5,8]
    # Create a variable to use as an accumulator.

    total = 0
    # Calculate the total of the list elements.
    for value in books:
        total += value
# Display the total of the list elements.
    print(f'The total of the elements is {total}.')

if __name__ == '__main__':
    main()
