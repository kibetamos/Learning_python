calories_burned_per_minute = 4.2

for minutes in range(10, 31, 5):
    calories_burned = calories_burned_per_minute * minutes
    print(f"After {minutes} minutes, you burned {calories_burned} calories.")
