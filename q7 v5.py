def flying(flightnum):
    flights = []
    # creates a list including the kilometres of each flight
    floyt = 1
    # base number to make the input more appealing
    while flightnum != 0:
        # this will only run if the user has taken flights
        while floyt <= flightnum:
            # this is so the program will stop asking for the user's kilometres after their last flight
            new_flight = int(input("How many kilometres was flight {} (including return)?: ".format(floyt)))
            floyt = floyt + 1
            flights.append(new_flight)
            # adds the users kilometres to the list
        if floyt >= flightnum:
            break
            # if the base number is greater or equal to the user's flights, the loop breaks
    total = sum(flights)
    return total


# main
valid = False
while not valid:
    flights_yes_no = input("Have you taken any flights this year?: ").lower()
    if flights_yes_no == "yes":
        flightnum = int(input("How many flights have you taken this year?: "))
        # asks the user how many flights they have taken this year and will use that number in the flying def
        total = flying(flightnum)
        print("\nYou have travelled a total of", total, "kms this year on plane")
        flight_emissions = .09
        # passenger flights emit around 0.09 kilograms of co2 per passenger kilometre
        total_flight_emissions = total * flight_emissions
        print("\nFrom air travel, you have emitted", total_flight_emissions, "kg of CO2 in the last year.")
        break
    elif flights_yes_no == "no":
        print("You have not taken any flights this year")
        break
    else:
        print("\nplease input yes or no")