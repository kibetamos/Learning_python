def main():
    #create a list of numbers

    numbers = [1,2,3,4,5,6,7]

    #open a file to write to
    outfile = open('numberlist.txt', 'w')

    #write list to the file
    for item in numbers:
        outfile.write(str(item) + '\n')

    outfile.close()


#call main function
if __name__ == '__main__':
    main()

