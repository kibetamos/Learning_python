# This program demonstrates how to get the
# index of an item in a list and then replace
# that item with a new item

def main():
    #lets create a list
    food = ['pizza','maize','ugali']

    #lets show items in the list

    print('Our list has the following')
    print(food)

    #get item to change
    item = input('Which item should i Change ?')

    try:
        item_index = food.index(item)
        
        #Replace
        new_item = input(' Enter new value: ')

        food[item_index] = new_item

        #Display the list
        print('Here is the revised list')

        print(food)

    except ValueError:
        print('That item was not found in the list')

#call the main function
        
if __name__ == '__main__':
    main()