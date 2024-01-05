# 3. Budget Analysis
'''
Write a program that asks the user to enter the amount that he or she has budgeted for
a month. A loop should then prompt the user to enter each of his or her expenses for the
month and keep a running total. When the loop finishes, the program should display the
amount that the user is over or under budget.
'''
def budget_analysis():

    total_expenses = 0

    budget = float(input("Enter the budgeted amount for the month: KES "))
    while True:
        try:
            expense = float(input("Enter an expense (enter 0 to finish): KES "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Check if the user wants to finish entering expenses
        if expense == 0:
            break

        # Add the entered expense to the total
        total_expenses += expense

    # Calculate the difference between the budget and total expenses
    difference = budget - total_expenses

    # Display the budget analysis result
    if difference == 0:
        print("You have spent exactly your budget. Well done!")
    elif difference > 0:
        print(f"You are under budget by KES {abs(difference):.2f}.")
    else:
        print(f"You are over budget by KES {abs(difference):.2f}.")

# Run the budget_analysis function
budget_analysis()

