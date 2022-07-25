def validate_float(prompt):
    while True:
        try:
            float_input = float(input(prompt))
            return float_input
        except ValueError:
            print("Please input a number ")

def main_transport(transport):
    # this def asks the user what their main form of transport is
    valid = False
    while not valid:
        try:
            if transport == "car":
                car_type = input("""\nWhat type of car do you travel in?
- Petrol
- Diesel
- Electric
""").lower()
                if car_type in ["petrol", "diesel", "electric"]:
                    return car_type
                else:
                    print("please input petrol, diesel or electric")
            elif transport == "bus":
                how_often = validate_float("""\nHow many times a week do you use the bus? (if once per day type 7, if twice a day type 14)\n""")
                km_per_ride = validate_float("\nRoughly how many kilometres is one bus ride")
                bus_per_year = how_often * 52 * km_per_ride
                print("You travel around", bus_per_year, "kilometers per year in a bus")
                bus_emissions = bus_per_year * 105
                # user_emissions = bus_emissions / 20 - don't need this as value is per passenger
                # there is an average of around 20 people on a bus when travelling to and from work or school, so I have divided the emissions among the passengers
                print("you emit", bus_emissions, "per year")
                # emissions = 822gm / km
                return bus_emissions
            elif transport == "train":
                how_often = validate_float("""\nHow many times a week do you use the train? (if once per day type 7, if twice a day type 14)\n""")
                km_per_ride = validate_float("Roughly how many kilometres is one train ride?: ")
                train_per_year = how_often * 52 * km_per_ride
                print("You travel around", train_per_year, "kilometers per year in a bus")
                train_emissions = train_per_year * 0.041
                # emissions = 0.041kg/km
                # user_emissions = train_emissions / 20  - don't need this as value is per passenger
                print("By travelling on train, you emit", train_emissions, "kilograms of CO2 per year")
                return train_emissions
        except ValueError:
            print("Please enter a number")

def q2(car_type):
    valid = False
    while not valid:
        try:
            while car_type in ["diesel", "electric", "petrol"]:
                km_per_week = validate_float("\nHow many kilometres do you drive per week?\n")
                #use km per week instead of minutes for easy calculations
                per_year = km_per_week * 52
                print("\nYou drive for", km_per_week, "kilometres per week, which is around", per_year, "kilometres per year")
                return per_year
        except ValueError:
            print("please enter a number")

def q3(per_year):
    petrol_emissions = 192
    #the average petrol car emits 192 grams of co2 per km.
    diesel_emissions = 171
    #the average diesel car emits 171 grams of co2 per km.
    if car_type == "petrol":
        total_emissions = per_year * petrol_emissions
        total_emissions_in_kg = total_emissions/1000
        total_emissions_in_tonnes = total_emissions_in_kg/1000
        print("With a petrol car, you are emitting around" , total_emissions, "grams of CO2 per year. This is", total_emissions_in_tonnes, "tonnes of CO2 per year.")
        return total_emissions
    elif car_type == "diesel":
        total_emissions = per_year * diesel_emissions
        total_emissions_in_kg = total_emissions / 1000
        total_emissions_in_tonnes = total_emissions_in_kg / 1000
        print("With a diesel car, you are emitting around" , total_emissions, "grams of CO2 per year. This is", total_emissions_in_tonnes, "tonnes of CO2 per year.")
        return total_emissions
    elif car_type == "electric":
        print("With an electric car, you are emitting no CO2 at all! This is great for the environment")

def electricity(monthly_household_electricity_usage, family_members):
    individual_electricity = monthly_household_electricity_usage/family_members
    print("\nBy yourself, you use around", individual_electricity,"kwH of electricity per month")
    yearly_individual_electricity = individual_electricity * 12
    print("This is", yearly_individual_electricity, "kwH of electricity per year")
    electricity_emissions = 0.39
    # 0.39 kg of CO2 per kwH
    total_electricity_emissions = yearly_individual_electricity * electricity_emissions
    return total_electricity_emissions

def gas():
    valid = False
    while not valid:
        try:
            gas_type = input("""\nwhat size gas bottles do you use:
- 9kg LPG bottles
- 45kg LPG bottles
- Both?: """).lower()
            if gas_type in ["9", "9kg"]:
                bottle_size = 9
                gas_per_month = validate_float("\nhow many bottles do you use per month?")
                print(gas_per_month)
                total_gas = bottle_size * gas_per_month
                print("you use", total_gas, "kg of gas per month")
                break
            elif gas_type in ["45", "45kg"]:
                bottle_size = 45
                gas_per_month = validate_float("\nhow many bottles do you use per month?")
                print(gas_per_month)
                total_gas = bottle_size * gas_per_month
                print("you use", total_gas, "kg of gas per month")
                yearly_gas = total_gas * 12
                print("this is", yearly_gas, "kg of gas per year")
                break
            else:
                print("please enter one of these")
            print(gas_type)
        except ValueError:
            print("no")

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

# main starts here

valid = False
while not valid:
    transport = input("""What is your main form of transport?:
    - Car
    - Bus
    - Walk
    - Bike
    - Train
    - Motorcycle
""").lower()
    if transport == "car":
        #should accept upper case or lower
        car_type = main_transport(transport)
        per_year = q2(car_type)
        total_emissions = q3(per_year)
        break
    elif transport == "bus":
        how_often = main_transport(transport)
        break
    elif transport in ["bike", "walk"]:
        print("Nice, you're already helping the environment!")
        break
    elif transport == "train":
        how_often = main_transport(transport)
        break
    else:
        print("Please input car, bus, walk or bike: ")

valid = False
while not valid:
    does_user_know_electricity = input("\nDo you know how much electricity you user per month (if no, we will use the average): ")
    if does_user_know_electricity == "yes":
        monthly_household_electricity_usage = validate_float("How much electricity does your household use monthly in kWh (check your electric bill)")
        family_members = validate_float("How many people live in your house?")
        total_electricity_emissions = electricity(monthly_household_electricity_usage, family_members)
        print("From your electricity usage, you emit", total_electricity_emissions, "kg of CO2")
        break
    elif does_user_know_electricity == "no":
        monthly_household_electricity_usage = 909
        print("\nThe average electricity usage of individuals in NZ is 909kWh per month")
        total_electricity_emissions = electricity(monthly_household_electricity_usage, 1)
        print("From your electricity usage, you emit", total_electricity_emissions, "kg of CO2")
        break
    else:
        print("\nPlease input yes or no")

valid = False
while not valid:
    gas_used = input("Do you use LPG gas at home?: ").lower()
    if gas_used == "yes":
        gas()
        break
    if gas_used == "no":
        break
    else:
        print("\nplease input yes or no")

valid = False
while not valid:
    flights_yes_no = input("Have you taken any flights this year?: ").lower()
    if flights_yes_no == "yes":
        flightnum = validate_float("How many flights have you taken this year?: ")
        # asks the user how many flights they have taken this year and will use that number in the flying def
        total = flying(flightnum)
        print("\nYou have travelled a total of", total, "kilometres this year on plane")
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

# add run again
# round to 2 dp