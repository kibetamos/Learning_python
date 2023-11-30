#Get a number of seconds from the user

# seconds = float(input('Enter number of seconds'))

# Get a number of seconds from the user.
2 total_seconds = float(input('Enter a number of seconds: '))
3
4 # Get the number of hours.
5 hours = total_seconds // 3600
6
7 # Get the number of remaining minutes.
8 minutes = (total_seconds // 60) % 60
9
10 # Get the number of remaining seconds.
11 seconds = total_seconds % 60
12
13 # Display the results.
14 print('Here is the time in hours, minutes, and seconds:')
15 print('Hours:', hours)
16 print('Minutes:', minutes)
17 print('Seconds:', seconds)