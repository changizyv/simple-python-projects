# The user enters a number (seconds)
seconds = int(input("Please enter the number of seconds: "))

# Convert seconds to hours
hours = seconds // 3600
seconds %= 3600

# Convert the remaining seconds to minutes
minutes = seconds // 60

# Remaining seconds after division by minutes
seconds %= 60

print("Time equivalent to the entered number of seconds: ", hours, "hour(s) ", minutes, "minute(s) ", seconds, "second(s)")
