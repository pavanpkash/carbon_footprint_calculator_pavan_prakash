import time

# Functions go here


def instructions():
    print("""\nWelcome to the carbon footprint calculator!""")
    print("""\nThis program will calculate your carbon footprint, 
show you your emissions and how you can combat climate change""")
print("You will be asked a few questions about your day-to-day life and then we will give you some solutions.")


def validate_float(prompt):
    while True:
        try:
            float_input = float(input(prompt))
            if float_input > 0:
                return float_input
            elif float_input <= 0:
                print("Please input a number greater than 0")
                # user must input a number greater than 0
        except ValueError:
            print("Please input a number ")
            # user must input a number


def main_transport(transport):

    valid = False
    while not valid:
        try:
            if transport == "car":
                car_type = input("""\nWhat type of car do you travel in?:
- Petrol
- Diesel
- Electric
""").lower()
                # asks user whether they drive a petrol, diesel or electric car
                if car_type in ["petrol", "diesel", "electric"]:
                    return car_type
                else:
                    print("Please input petrol, diesel or electric.")
                    # if user inputs incorrectly, they will be asked to enter something correct
            elif transport == "bus":
                how_often = validate_float("""\nHow many times a week do you use the bus? 
(if once per day type 7, if twice a day type 14): """)
                # if the user uses a bus, they will be asked how often they use the bus
                km_per_ride = validate_float("\nRoughly how many kilometres is one bus ride.")
                bus_per_year_unrounded = how_often * 52 * km_per_ride
                bus_per_year = round(bus_per_year_unrounded)
                # will then figure out how many times per year they use the bus
                print("You travel around", bus_per_year, "kilometers per year in a bus.")
                vehicle_emissions_unrounded = bus_per_year * 0.105
                vehicle_emissions = round(vehicle_emissions_unrounded)
                print("You emit", vehicle_emissions, "kilograms of CO2 per year.")
                # bus emissions = 0.105kg / km
                return vehicle_emissions
            elif transport == "train":
                how_often = validate_float("""\nHow many times a week do you use the train? 
(if once per day type 7, if twice a day type 14): """)
                km_per_ride = validate_float("Roughly how many kilometres is one train ride?: ")
                # asks user how often and how long their train rides are
                train_per_year_unrounded = how_often * 52 * km_per_ride
                train_per_year = round(train_per_year_unrounded)
                # multiply weekly train rides by 52 to find yearly km
                print("You travel around", train_per_year, "kilometers per year in a train.")
                vehicle_emissions_unrounded = train_per_year * 0.041
                vehicle_emissions = round(vehicle_emissions_unrounded)
                # train emissions = 0.041kg/km
                print("By travelling on train, you emit", vehicle_emissions, "kilograms of CO2 per year.")
                return vehicle_emissions
            elif transport == "motorcycle":
                km_per_week_unrounded = validate_float("\nHow many kilometres do you ride per week?: \n")
                km_per_week = round(km_per_week_unrounded)
                per_year = km_per_week * 52
                print("\nYou drive for", km_per_week, "kilometres per week, "
                      "which is around", per_year, "kilometres per year.")
                vehicle_emissions_unrounded = per_year * 0.103
                vehicle_emissions = round(vehicle_emissions_unrounded)
                # motorcycle emissions = 0.103kg/km
                return vehicle_emissions

        except ValueError:
            print("Please enter a number: ")


def fuel(car_type):
    valid = False
    while not valid:
        try:
            while car_type in ["diesel", "electric", "petrol"]:
                km_per_week_unrounded = validate_float("\nHow many kilometres do you drive per week?: \n")
                km_per_week = round(km_per_week_unrounded)
                per_year = km_per_week * 52
                print("\nYou drive for", km_per_week, "kilometres per week, "
                      "which is around", per_year, "kilometres per year.")
                # calculate km driven per year
                return per_year
        except ValueError:
            print("Please enter a number: ")


def q3(car_type, per_year):
    petrol_emissions = 0.192
    # the average petrol car emits 0.192 kg of co2 per km.
    diesel_emissions = 0.171
    # the average diesel car emits 0.171 kg of co2 per km.
    if car_type == "petrol":
        vehicle_emissions_unrounded = per_year * petrol_emissions
        # multiply petrol emissions by km per year
        vehicle_emissions = round(vehicle_emissions_unrounded)
        # round is used throughout the program to give an appealing round number with no dp
        time.sleep(1)
        print("With a petrol car, you are emitting around", vehicle_emissions, "kilograms of CO2 per year.")
        return vehicle_emissions
    elif car_type == "diesel":
        vehicle_emissions_unrounded = per_year * diesel_emissions
        # multiply diesel emissions by km per year
        vehicle_emissions = round(vehicle_emissions_unrounded)
        time.sleep(1)
        print("With a diesel car, you are emitting around", vehicle_emissions, "kilograms of CO2 per year.")
        return vehicle_emissions
    elif car_type == "electric":
        print("With an electric car, you are emitting no CO2 at all! This is great for the environment.")
        vehicle_emissions = 0
        return vehicle_emissions


def individual_vehicle_emission_calculator(transport):
    if transport == "car":
        # should accept upper case or lower
        car_type = main_transport(transport)
        per_year = fuel(car_type)
        vehicle_emissions = q3(car_type, per_year)
        # when the user selects this transport, every other transport will = 0 for easy calculations
        # this applies for every selectable transport
        return vehicle_emissions

    elif transport == "bus":
        vehicle_emissions = main_transport(transport)
        return vehicle_emissions

    elif transport in ["bike", "walk"]:
        print("Nice, you're already helping the environment!")
        vehicle_emissions = 0
        return vehicle_emissions

    elif transport == "train":
        vehicle_emissions = main_transport(transport)
        return vehicle_emissions

    elif transport == "motorcycle":
        vehicle_emissions = main_transport(transport)
        return vehicle_emissions
    else:
        print("Please input car, bus, walk, bike, train or motorcycle: ")


def total_vehicle_emission_calculator():
    # This function asks the user what their main form of transport is
    valid = False
    while not valid:
        transport = input("""\nWhat is your main form of transport?:
- Car
- Bus
- Walk
- Bike
- Train
- Motorcycle\n""").lower()
        if transport in ["car", "bus", "train", "walk", "bike", "motorcycle"]:
            vehicle_emissions = individual_vehicle_emission_calculator(transport)
            return vehicle_emissions
        # if the transport is one of the listed options, it will use the final_vehicle_emission_calculator function
        else:
            print("Please enter a valid value")


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


def electricity(monthly_household_electricity_usage, family_members):
    individual_electricity_unrounded = monthly_household_electricity_usage/family_members
    # divides monthly electricity by family members to find individual electricity usage per month
    individual_electricity = round(individual_electricity_unrounded)
    print("\nBy yourself, you use around", individual_electricity, "kwH of electricity per month")
    yearly_individual_electricity = individual_electricity * 12
    # multiply by 12 to find electricity usage per year
    time.sleep(2)
    print("\nThis is", yearly_individual_electricity, "kwH of electricity per year")
    electricity_emissions = 0.39
    # 0.39 kg of CO2 per kwH
    total_electricity_emissions_unrounded = yearly_individual_electricity * electricity_emissions
    total_electricity_emissions = round(total_electricity_emissions_unrounded)
    # multiply by 0.39 to find emissions per year from electricity usage
    return total_electricity_emissions


def other_trial():
    valid = False
    while not valid:
        does_user_know_electricity = yes_no(
            "\nDo you know how much electricity you user per month (if no, we will use the average): ")
        # asks user if they know their electricity usage
        # this is mainly for the younger audience who may not know their electricity usage
        if does_user_know_electricity == "yes":
            monthly_household_electricity_usage = validate_float("\nHow much electricity"
                                                                 " does your household use monthly"
                                                                 " in kWh (check your electric bill)")
            # asks for monthly household electricity usage
            family_members = validate_float("\nHow many people live in your house?: ")
            # asks for how many people they share the house with
            total_electricity_emissions = electricity(monthly_household_electricity_usage, family_members)
            return total_electricity_emissions
        elif does_user_know_electricity == "no":
            monthly_household_electricity_usage = 909
            # average monthly electricity usage for an individual is 909 kWh
            print("\nThe average electricity usage of individuals in NZ is 909kWh per month. ")
            total_electricity_emissions = electricity(monthly_household_electricity_usage, 1)
            return total_electricity_emissions


def gas():
    valid = False
    while not valid:
        try:
            gas_type = input("""\nWhat size gas bottles do you use:
- 9kg LPG bottles
- 45kg LPG bottles
- Both?: """).lower()
            # asks user what size gas bottles they use
            if gas_type in ["9", "9kg"]:
                bottle_size = 9
                # 1kg of lpg gas is 2.95 kg of CO2
                gas_per_month = validate_float("\nHow many bottles do you use per month?: ")
                # asks user how many 9kg bottles they use per month
                total_gas_unrounded = bottle_size * gas_per_month
                total_gas = round(total_gas_unrounded)
                print("\nYou use", total_gas, "kilograms of gas per month")
                yearly_gas = total_gas * 12
                time.sleep(1)
                print("This is", yearly_gas, "kilograms of gas per year")
                co2_from_gas_unrounded = yearly_gas * 2.95
                co2_from_gas = round(co2_from_gas_unrounded)
                return co2_from_gas
            elif gas_type in ["45", "45kg"]:
                bottle_size = 45
                gas_per_month = validate_float("\nHow many bottles do you use per month?: ")
                # asks user how many 45kg bottles they use per month
                total_gas_unrounded = bottle_size * gas_per_month
                total_gas = round(total_gas_unrounded)
                print("\nYou use", total_gas, "kg of gas per month")
                yearly_gas = total_gas * 12
                time.sleep(1)
                print("This is", yearly_gas, "kg of gas per year")
                co2_from_gas_unrounded = yearly_gas * 2.95
                co2_from_gas = round(co2_from_gas_unrounded)
                return co2_from_gas
            elif gas_type in ["both", "b"]:
                forty_five_per_month = validate_float("\nHow many 45kg bottles do you use per month?: ")
                # asks user how many 45kg bottles they use per month
                nine_per_month = validate_float("\nHow many 9kg bottles do you use per month?: ")
                # asks user how many 9kg bottles they use per month
                forty_five_bottle_size = 45
                nine_bottle_size = 9
                total_nine_gas = nine_bottle_size * nine_per_month
                total_forty_five_gas = forty_five_bottle_size * forty_five_per_month
                combined_gas_unrounded = total_forty_five_gas + total_nine_gas
                combined_gas = round(combined_gas_unrounded)
                print("\nYou use", combined_gas, "kilograms of gas in one month.")
                yearly_combined_gas = combined_gas * 12
                time.sleep(1)
                print("This is", yearly_combined_gas, "kilograms of gas per year.")
                co2_from_gas_unrounded = yearly_combined_gas * 2.95
                co2_from_gas = round(co2_from_gas_unrounded)
                return co2_from_gas
            else:
                print("\nPlease enter one of these")
        except ValueError:
            print("no")


def gas_yes_no():
    valid = False
    while not valid:
        gas_used = yes_no("\nDo you use LPG gas at home?: ")
        # asks user if they use LPG gas as some do not
        if gas_used == "yes":
            co2_from_gas = gas()
            return co2_from_gas
        elif gas_used == "no":
            break


def flying(flightnum):
    flights = []
    # creates a list including the kilometres of each flight
    base_num = 1
    # base number to make the input more appealing
    while flightnum != 0:
        # this will only run if the user has taken flights
        while base_num <= flightnum:
            # this is so the program will stop asking for the user's kilometres after their last flight
            new_flight = validate_float("How many kilometres was flight {} (including return)?: ".format(base_num))
            base_num = base_num + 1
            flights.append(new_flight)
            # adds the users kilometres to the list
        if base_num >= flightnum:
            break
            # if the base number is greater or equal to the user's flights, the loop breaks
    total = sum(flights)
    return total


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

# main starts here


use_again = True
while use_again:

    instructions()

    motorcycle_emissions = 0
    train_emissions = 0
    bus_emissions = 0
    total_car_emissions = 0
    final_vehicle_emissions = total_vehicle_emission_calculator()
    time.sleep(1)
    print("You emit a total of", final_vehicle_emissions, "kg of CO2 per year from day-to-day transport.")

    total_electricity_emissions = other_trial()
    time.sleep(2)
    print("\nFrom electricity usage, you emit", total_electricity_emissions, "kg of CO2 per year.")

    co2_from_gas = gas_yes_no()
    time.sleep(1)
    print("This is", co2_from_gas, "kilograms of CO2 per year.")

    total_flight_emissions = yesno_flights()
    time.sleep(1)
    print("\nFrom air travel, you have emitted", total_flight_emissions, "kilograms of CO2 in the last year.")

    carbon_footprint = final_vehicle_emissions + total_electricity_emissions + co2_from_gas + total_flight_emissions
    print("Your total carbon footprint is", carbon_footprint, "kg of CO2 emitted per year.")

    play_again = yes_no("Would you like to run the program again?: ")
    if play_again == "yes":
        use_again = True
    elif play_again == "no":
        use_again = False
