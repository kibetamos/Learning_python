def main():
    count = 0

    my_string = input('Enter a sentence: ')

    for ch in my_string:
        if ch == 'T' or ch == 't':
            count +=1

    print(f'The letter T appears {count} times.')


if __name__ == '__main__':
    main()

