#Get a number of seconds from the user

seconds = float(input('Enter number of seconds'))

# Get a number of seconds from the user.total_seconds = float(input('Enter a number of seconds: ')# Get the number of hours.hours = total_seconds // 360# Get the number of remaining minutes.minutes = (total_seconds // 60) % 6
# Get the number of remaining seconds.
seconds = seconds % 60
# Display the results.
print('Here is the time in hours, minutes, and seconds:')
print('Hours:', hours)
print('Minutes:', minutes)
print('Seconds:', seconds)