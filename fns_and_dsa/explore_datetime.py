from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

number_of_days = input("Enter the number of days to add to the current date: ")
number_of_days = int(number_of_days)

def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)  # Using the function parameter
    return future_date

display_current_datetime()
future_date = calculate_future_date(number_of_days)
print("Future date:", future_date.strftime("%Y-%m-%d %H:%M:%S"))