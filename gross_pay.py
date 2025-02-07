# Define "compute pay" function
def computepay(hours,rate) :

    try:

        # Convert string values to float
        hours = float(hours)
        rate = float(rate)

    except:
        print("Please review the entered data.")
        quit()

    # Calculate gross pay
    grossPay = round(hours * rate, 2)

    # If user worked more than 40 hours in the week, calculate overtime pay
    if hours > 40:
        grossPay = round((rate * 40) + (hours - 40) * (rate * 1.5), 2)
        overPay = round((hours - 40) * (rate * 1.5), 2)

        # Print gross pay
        print("Your gross pay is: $" + str(grossPay) + ".")
        print("You were paid $" + str(overPay) + " of overtime pay.")

    else:
        # Print gross pay (no overtime)
        print("Your gross pay is: $" + str(grossPay))

# Prompt the user for weekly hours worked and hourly rate
weeklyHours = input("Weekly hours worked? ")
hourlyRate = input("Hourly pay rate? ")
computepay(weeklyHours,hourlyRate)