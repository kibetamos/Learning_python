def main():

    count = 0

    my_string = input('Enter a sentence: ')
    
    for ab in my_string:
        if ab =='A' or ab == 'a':
            count += 1

    print(f'The letter A appears { count } times')

if __name__ == '__main__':
    main()

    