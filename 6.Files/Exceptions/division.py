

def main():
    #lets get numbers to devide
    a = int(input('Enter number A: '))

    b = int(input('Enter number b: '))

    if b !=0:
        
        divide = a/b

        print(f'{a} divided by {b} is {divide}')
    else:
        print('Cannot divide by 0')

if __name__ == '__main__':
    main()