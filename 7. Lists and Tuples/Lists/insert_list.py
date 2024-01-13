#This demonstrates the insert method
def main():
    #creare a list of names 
    students = ['mark', 'Amos', 'Kibet']
    print('The students are ',students)

    new_name = input('Whats the new name you want to add ')

    students.insert(0, new_name)

    #The list after insert
    print('the Students are', students)

if __name__ == '__main__':
    main()