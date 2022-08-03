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


def validate_float(prompt):
    while True:
        try:
            float_input = float(input(prompt))
            return float_input
        except ValueError:
            print("Please input a number ")


# asks user if they have taken any flights this year
def yesno_flights():
    flights_yes_no = yes_no("\nHave you taken any flights this year?: ")
    if flights_yes_no == "yes":
        flight_num = validate_float(
            "\nHow many flights have you taken this year?: ")
        # asks the user how many flights they have taken this year
        total = round(flight_distance_calculator(flight_num))
        print("\nYou have travelled a total of", total,
              "kilometres this year on plane.")
        flight_emissions = .09
        # flights emit 0.09 kilograms of co2 per passenger kilometre
        total_flight_emissions = round(total * flight_emissions)
        return total_flight_emissions
    elif flights_yes_no == "no":
        total_flight_emissions = 0
        print("You have not taken any flights this year")
        return total_flight_emissions
    else:
        print("\nPlease input yes or no")


# asks user how many kilometres each flight was, depending on user input
def flight_distance_calculator(flight_num):
    flights = []
    # creates a list including the kilometres of each flight
    base_num = 1
    # base number to make the input more appealing
    while flight_num != 0:
        # this will only run if the user has taken flights
        while base_num <= flight_num:
            # program will stop asking for the user's kilometres,
            # after their last flight
            new_flight = validate_float(
                "How many kilometres was flight "
                "{} (including return)?: ".format(base_num))
            base_num = base_num + 1
            flights.append(new_flight)
            # adds the users kilometres to the list
        if base_num >= flight_num:
            break
            # if the base number is greater or equal to the user's flights,
            # the loop breaks
    total = sum(flights)
    return total


# main

total_flight_emissions = yesno_flights()
time.sleep(1)
print("From air travel, you have emitted", total_flight_emissions,
      "kilograms of CO2 in the last year.")
