'''
If you have downloaded the source code you will find a file named USPopulation.txt
in the Chapter 07 folder. The file contains the midyear population of the United States, in
thousands, during the years 1950 through 1990. The first line in the file contains the popu-
lation for 1950, the second line contains the population for 1951, and so forth.
Write a program that reads the file’s contents into a list. The program should display the
following data:
• The average annual change in population during the time period
• The year with the greatest increase in population during the time period
• The year with the smallest increase in population during the time period

'''

def main():
    file_path = 'Chapter 07/USPopulation.txt'
    population_data = read_population_data(file_path)

    average_change = calculate_average_annual_change(population_data)
    greatest_increase_year = find_greatest_increase(population_data)
    smallest_increase_year = find_smallest_increase(population_data)

    print(f'Average Annual Change in Population: {average_change:.2f} thousand')
    print(f'Year with Greatest Increase: {greatest_increase_year}')
    print(f'Year with Smallest Increase: {smallest_increase_year}')

def read_population_data(file_path):
    with open(file_path, 'r') as file:
        population_data = [int(line.strip()) for line in file]
    return population_data

def calculate_average_annual_change(population_data):
    total_change = 0
    for i in range(1, len(population_data)):
        total_change += population_data[i] - population_data[i - 1]
    
    average_change = total_change / (len(population_data) - 1)
    return average_change

def find_greatest_increase(population_data):
    max_increase = max(population_data[i] - population_data[i - 1] for i in range(1, len(population_data)))
    max_increase_index = population_data.index(max_increase + population_data[0])
    return max_increase_index + 1951

def find_smallest_increase(population_data):
    min_increase = min(population_data[i] - population_data[i - 1] for i in range(1, len(population_data)))
    min_increase_index = population_data.index(min_increase + population_data[0])
    return min_increase_index + 1951



if __name__ == "__main__":
    main()
