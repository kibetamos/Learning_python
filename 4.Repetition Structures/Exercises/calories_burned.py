#2. Calories Burned
'''
Running on a particular treadmill you burn 4.2 calories per minute. Write a program that
uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.
'''
calories_burned_per_minute = 4.2

for minutes in range(10, 31, 5):
    calories_burned = calories_burned_per_minute * minutes
    print(f"After {minutes} minutes, you burned {calories_burned} calories.")
