def main():
    #open file for reading
    infile = open('numberlist.txt', 'r')

    #read the contentes of the file into a list

    numbers = infile.readlines()

    #close file
    infile.close()

    for index in range(len(numbers)):
        numbers[index]= int(numbers[index])

        #print the contents of the list
    print(numbers)

#call main function
if __name__ == '__main__':
    main()

