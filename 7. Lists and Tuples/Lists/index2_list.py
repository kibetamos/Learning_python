
#lets create a list
comp = ['hp', 'samsung', 'dell', 'Lenovo']

def main():
    #lets get the list printed out
    print('Here are your computers')

    print(comp)

    #lets get the comuter we want to change
    item = input('Which computer do you want to change')

    try:
        item_index = comp.index(item)

        #lets replace it
        new_comp = input('Whats the new computer')

        comp[item_index] = new_comp

        print('Here is our new comp mlist')

        print(comp)

    except ValueError as err:
        print(err)

        
if __name__ == '__main__':
    main()