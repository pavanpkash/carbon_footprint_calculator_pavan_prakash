import time

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        # the response that the user gives will be changed to lowercase
        if response == "yes" or response == "y":
            response = "yes"
        # if the user inputs y or yes, the program continues
            return response
        elif response == "no" or response == "n":
            response = "no"
        # if the user inputs n or no, instructions are shown
            return response
        else:
            print("Please answer yes / no")
        # if the user inputs anything else, they are told to answer yes or no

def flying(flightnum):
    flights = []
    # creates a list including the kilometres of each flight
    floyt = 1
    # base number to make the input more appealing
    while flightnum != 0:
        # this will only run if the user has taken flights
        while floyt <= flightnum:
            # this is so the program will stop asking for the user's kilometres after their last flight
            new_flight = validate_float("How many kilometres was flight {} (including return)?: ".format(floyt))
            floyt = floyt + 1
            flights.append(new_flight)
            # adds the users kilometres to the list
        if floyt >= flightnum:
            break
            # if the base number is greater or equal to the user's flights, the loop breaks
    total = sum(flights)
    return total

def validate_float(prompt):
    while True:
        try:
            float_input = float(input(prompt))
            return float_input
        except ValueError:
            print("Please input a number ")

def yesno_flights():
    valid = False
    while not valid:
        flights_yes_no = yes_no("\nHave you taken any flights this year?: ")
        if flights_yes_no == "yes":
            flightnum = validate_float("\nHow many flights have you taken this year?: ")
            # asks the user how many flights they have taken this year and will use that number in the flying def
            total_unrounded = flying(flightnum)
            total = round(total_unrounded)
            print("\nYou have travelled a total of", total, "kilometres this year on plane.")
            flight_emissions = .09
            # passenger flights emit around 0.09 kilograms of co2 per passenger kilometre
            total_flight_emissions_unrounded = total * flight_emissions
            total_flight_emissions = round(total_flight_emissions_unrounded)
            return total_flight_emissions
        elif flights_yes_no == "no":
            print("You have not taken any flights this year")
            break
        else:
            print("\nPlease input yes or no")
# main

total_flight_emissions = yesno_flights()
time.sleep(1)
print("\nFrom air travel, you have emitted", total_flight_emissions, "kilograms of CO2 in the last year.")