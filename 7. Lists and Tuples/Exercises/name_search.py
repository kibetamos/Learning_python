def read_names(file_path):
    with open(file_path, 'r') as file:
        names = [line.strip() for line in file]
    return names

def display_most_popular_names(names, gender):
    print(f"\nTop 5 Most Popular {gender} Names:")
    for i in range(5):
        print(f"{i + 1}. {names[i]}")

def main():
    girl_names_path = '/home/amos/projects/PYTHON/7. Lists and Tuples/Exercises/GirlNames.txt'
    boy_names_path = '/home/amos/projects/PYTHON/7. Lists and Tuples/Exercises/BoyNames.txt'

    girl_names = read_names(girl_names_path)
    boy_names = read_names(boy_names_path)

    display_most_popular_names(girl_names, 'Girl')
    display_most_popular_names(boy_names, 'Boy')

if __name__ == "__main__":
    main()
