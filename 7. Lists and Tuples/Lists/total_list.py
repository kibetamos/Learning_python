#Calculates the total of the sum of values in a list

def main():
    books = [50,2,4,5,8]
    total = 0
    for value in books:
        total += value

    print(f'The total of the elements is {total}.')

if __name__ == '__main__':
    main()
