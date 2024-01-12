#we have a constat that hold the number of days that we will gather sales
num_days = 5

def main():
    #a list to hold  sales for @ day
    sales = [0] *num_days

    print('Enter the sales for each day')

    #get the sales for each day
    
    for index in range(len(sales)):
        sales[index] = float(input(f'Day #{index + 1}'))

    #Display values entered
    print('Here are the values you entered')

    for value in sales:
        print(value)
    

#call main function
if __name__ == '__main__':
    main()