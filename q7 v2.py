def flightsp(flights):
    while flights > 0:
        print(flights)
        flightyy = int(input("how many kilometres was flight"))
        flights = flights - 1
        print(flights)
        return flights

#main
flights = int(input("how many flights have you had in the last year"))
flightsp(flights)

print("fin")