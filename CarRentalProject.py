import math

BANNER = "\nWelcome to Horizons car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BD, D, W) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)"

print(BANNER)

prompt = input("\nWould you like to continue (A/B)? \n")
#if prompt == "B":
    #print("Thank you for your loyalty.")
#elif prompt == "A":
while prompt == "A":
    cust_code = input("\nCustomer code (BD, D, W): \n")
    while not(cust_code == 'BD' or cust_code == 'D' or cust_code == 'W'):
        print("\n\t*** Invalid customer code. Try again. ***")
        cust_code = input("\nCustomer code (BD, D, W): \n")
    if cust_code == "BD":
        num_days = int(input("\nNumber of days: \n"))
        odometer_start = int(input("Odometer reading at the start: \n"))
        odometer_end = int(input("Odometer reading at the end:   \n"))
        if (1000000 - odometer_start) <= odometer_end:
            miles_calc = ((1000000 - odometer_start) + (odometer_end)) / 10
            amount_due = (40 * num_days) + (miles_calc * .25)
            print("\nCustomer summary:")
            print("\tclassification code:", cust_code)
            print("\trental period (days):", num_days)
            print("\todometer reading at start:", odometer_start)
            print("\todometer reading at end:  ", odometer_end)
            print("\tnumber of miles driven: ", miles_calc)
            print("\tamount due: $", float(amount_due))
        else:
            miles_calc = (odometer_end - odometer_start) / 10
            amount_due = (40 * num_days) + (miles_calc * .25)
            print("\nCustomer summary:")
            print("\tclassification code:", cust_code)
            print("\trental period (days):", num_days)
            print("\todometer reading at start:", odometer_start)
            print("\todometer reading at end:  ", odometer_end)
            print("\tnumber of miles driven: ", miles_calc)
            print("\tamount due: $", float(amount_due))
        #prompt = input("\nWould you like to continue (A/B)? \n")
    elif cust_code == "D":
        num_days = int(input("\nNumber of days: \n"))
        odometer_start = int(input("Odometer reading at the start: \n"))
        odometer_end = int(input("Odometer reading at the end:   \n"))
        miles_calc = (odometer_end - odometer_start) / 10
        if (miles_calc / num_days) <= 100:
            amount_due = (60 * num_days)
            print("\nCustomer summary:")
            print("\tclassification code:", cust_code)
            print("\trental period (days):", num_days)
            print("\todometer reading at start:", odometer_start)
            print("\todometer reading at end:  ", odometer_end)
            print("\tnumber of miles driven: ", miles_calc)
            print("\tamount due: $", float(amount_due))
            #prompt = input("\nWould you like to continue (A/B)? \n")
        else:
            amount_due = (60 * num_days) + ((miles_calc - (100*num_days)) * 0.25)
            print("\nCustomer summary:")
            print("\tclassification code:", cust_code)
            print("\trental period (days):", num_days)
            print("\todometer reading at start:", odometer_start)
            print("\todometer reading at end:  ", odometer_end)
            print("\tnumber of miles driven: ", miles_calc)
            print("\tamount due: $", float(amount_due))
    elif cust_code == "W":
        num_days = int(input("\nNumber of days: \n"))
        odometer_start = int(input("Odometer reading at the start: \n"))
        odometer_end = int(input("Odometer reading at the end:   \n"))
        miles_calc = (odometer_end - odometer_start) / 10
        weeks_calc = num_days / 7
        weeks = math.ceil(weeks_calc)
        avg_miles_day = (miles_calc / num_days)
        avg_miles_week = (miles_calc / weeks)
        if avg_miles_week <= 900:
            amount_due = weeks * 190
            print("\nCustomer summary:")
            print("\tclassification code:", cust_code)
            print("\trental period (days):", num_days)
            print("\todometer reading at start:", odometer_start)
            print("\todometer reading at end:  ", odometer_end)
            print("\tnumber of miles driven: ", miles_calc)
            print("\tamount due: $", float(amount_due))
        elif avg_miles_week >= 901 and avg_miles_week <= 1500:
            amount_due = (190 * weeks) + (100 * weeks)
            print("\nCustomer summary:")
            print("\tclassification code:", cust_code)
            print("\trental period (days):", num_days)
            print("\todometer reading at start:", odometer_start)
            print("\todometer reading at end:  ", odometer_end)
            print("\tnumber of miles driven: ", miles_calc)
            print("\tamount due: $", float(amount_due))
        elif avg_miles_week >= 1501:
            amount_due = (190 * weeks) + (200 * weeks) + ((miles_calc - (1500*weeks)) * 0.25)
            print("\nCustomer summary:")
            print("\tclassification code:", cust_code)
            print("\trental period (days):", num_days)
            print("\todometer reading at start:", odometer_start)
            print("\todometer reading at end:  ", odometer_end)
            print("\tnumber of miles driven: ", miles_calc)
            print("\tamount due: $", float(amount_due))
    prompt = input("\nWould you like to continue (A/B)? \n")
    #cust_code = input("\nCustomer code (BD, D, W): \n")
print("Thank you for your loyalty.")