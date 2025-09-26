from datetime import datetime, timedelta

#Function to display the current date and time
def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

# Function to calculate_future_date(days):
    future_date = datetime.now() + timedelta(days=days)
    return future_date

#Main function to interact with the user
def main():
    display_current_datetime()
    while True:
        try:
            days = int(input("Enter the number of days to add to the current date: "))
            future_date = calculate_future_date(days)
            print(f"Future date:", future_date.strftime("%Y-%m-%d %H:%M:%S"))
            break
        except ValueError:
            print("Please enter a valid number of days.")

#Main function to run the program
if __name__ == "__main__":
    main()