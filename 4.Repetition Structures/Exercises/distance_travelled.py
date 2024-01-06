def distance_traveled():
    # Get the speed of the vehicle from the user
    speed = float(input("What is the speed of the vehicle in mph? "))

    # Get the number of hours the vehicle has traveled
    hours = int(input("How many hours has it traveled? "))

    # Display the table header
    print("\nHour  Distance Traveled")

    # Use a loop to calculate and display the distance for each hour
    for hour in range(1, hours + 1):
        distance = speed * hour
        print(f"{hour:<5}{distance:<15.2f}")

# Run the distance_traveled function
distance_traveled()