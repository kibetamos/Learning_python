# Average Rainfall 
'''
Write a program that uses nested loops to collect data and calculate the average rainfall over
a period of years. The program should first ask for the number of years. The outer loop will
iterate once for each year. The inner loop will iterate twelve times, once for each month.
Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
After all iterations, the program should display the number of months, the total inches of
rainfall, and the average rainfall per month for the entire period.

'''
def average_rainfall():
    #lets get the number of years from the user 
    num_years = int(input("Enter the number of years"))
    #lets  keep track of months and total rainfall
    total_rainfall = 0
    total_months=0

    for year in range(1, num_years + 1):
        # Inner loop for each month
        for month in range(1, 13):
            # Get the inches of rainfall for the current month
            rainfall = float(input(f"Enter the inches of rainfall for Year {year}, Month {month}: "))
            
            # Add the rainfall to the total
            total_rainfall += rainfall
            
            # Increment the total months
            total_months += 1

    # Calculate the average rainfall
    average_rainfall = total_rainfall / total_months

    # Display the results
    print("\nResults:")
    print(f"Total number of months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f} inches")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")

# Run the average_rainfall function
average_rainfall()