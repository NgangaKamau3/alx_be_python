from datetime import datetime
from datetime import timedelta

#Part 1: Obtain the current date and time

def display_current_datetime(current_date=None):
    """Display the current date and time. 
    Returns:
        The current date and time in the following format: YYYY-MM-DD HH:MM:SS as a statement logged to the console.
        """
    current_date = datetime.now()
    return f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}"

#Part 2: Calculate a future date
def calculate_future_date(number_of_days):
    """Calculate the date from a specified number of days in the future. 
    Input:
        number_of_days (int): The number of days to add to the current date. Entered by the user. 
    Returns:
        The future date in the following format: YYYY-MM-DD as a statement logged to the console.
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    return f"Future date after {number_of_days} days: {future_date.strftime('%Y-%m-%d')}"

#Wrapping it all up and creating a main function that allows a user to interact with the code. 

# Example output(hypothetical):
# Current date and time: 2024-03-25 15:30:45
# Enter the number of days to add to the current date: 10
# Future date: 2024-04-04

if __name__ == "__main__":
    print(display_current_datetime())
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    print(calculate_future_date(days_to_add))