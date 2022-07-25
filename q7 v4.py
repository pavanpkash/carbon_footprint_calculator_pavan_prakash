def flying(flightnum):
    flights = []
    while flightnum != 0:
        new_flight = int(input("how many kms was flight {} (including return)?: ".format(flightnum)))
        flightnum = flightnum - 1

        if new_flight != 0:
            flights.append(new_flight)
    total = sum(flights)
    return total



#main
flightnum = int(input("how many flights have you taken this year?: "))
total = flying(flightnum)
print("you have travelled a total of", total, "kms this year on plane")