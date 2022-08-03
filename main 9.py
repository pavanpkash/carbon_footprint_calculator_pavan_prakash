import time


# Functions go here
# This function makes sure that the user inputs yes or no
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


# This function makes sure the user has entered a number
def validate_float(prompt):
    while True:
        try:
            float_input = float(input(prompt))
            if float_input > 0:
                return float_input
            elif float_input <= 0:
                print("Please input a number greater than 0.")
                # user must input a number greater than 0
        except ValueError:
            print("Please input a number greater than 0.")
            # user must input a number


# This function displays instructions on how to use the program
def instructions():
    print("""\nWelcome to the carbon footprint calculator!""")
    time.sleep(1),
    print("\nThis program will calculate your carbon footprint, show you your "
          "emissions and give you solutions to combat climate change.")
    print("You will be asked a few questions about your day-to-day life "
          "and then we will give you some solutions.")


# This function asks the user what their main form of transport is
# and calculates total mileage for the year
def main_transport():
    valid = False
    while not valid:
        transport = validate_float("""\nWhat is your main form of transport?:
1) Car
2) Bus
3) Walk
4) Bike
5) Train
6) Motorcycle\n""")
        if transport == 1:
            # car
            vehicle_emissions = petrol_diesel_emissions()
            return vehicle_emissions

        elif transport == 2:
            # bus
            how_often = validate_float(
                "\nHow many times a week do you use the bus? "
                "(if once per day type 7, if twice a day type 14): ")
            # if the user uses a bus they will be asked how often
            km_per_ride = validate_float(
                "\nRoughly how many kilometres is one bus ride.")
            bus_per_year = round(how_often * 52 * km_per_ride)
            # round is used to give an appealing round number with no dp
            # will then figure out how many times per year they use the bus
            print("\nYou travel around", bus_per_year,
                  "kilometers per year in a bus.")
            vehicle_emissions = round(bus_per_year * 0.105)
            print("You emit", vehicle_emissions, "kilograms of CO2 per year.")
            # bus emissions = 0.105kg / km
            return vehicle_emissions

        elif transport in [3, 4]:
            # walk, bike
            print("Nice, you're already helping the environment!")
            vehicle_emissions = 0
            return vehicle_emissions

        elif transport == 5:
            # train
            how_often = validate_float(
                "\nHow many times a week do you use the train? "
                "(if once per day type 7, if twice a day type 14): ")
            km_per_ride = validate_float(
                "Roughly how many kilometres is one train ride?: ")
            # asks user how often and how long their train rides are
            train_per_year = round(how_often * 52 * km_per_ride)
            # multiply weekly train rides by 52 to find yearly km
            print("You travel around", train_per_year,
                  "kilometers per year in a train.")
            vehicle_emissions = round(train_per_year * 0.041)
            # train emissions = 0.041kg/km
            print("By travelling on train, you emit", vehicle_emissions,
                  "kilograms of CO2 per year.")
            return vehicle_emissions

        elif transport == 6:
            # motorcycle
            km_per_week = round(validate_float(
                "\nHow many kilometres do you ride per week?: \n"))
            per_year = km_per_week * 52
            print("\nYou drive for", km_per_week, "kilometres per week, "
                  "which is around", per_year,
                  "kilometres per year.")
            vehicle_emissions = round(per_year * 0.103)
            # motorcycle emissions = 0.103kg/km
            return vehicle_emissions
        else:
            print("Please input 1, 2, 3, 4, 5 or 6: ")


# this function asks user what type of car they travel in,
# calculates kilometres travelled per year,
# multiplies total mileage per year by the emissions of the chosen car
def petrol_diesel_emissions():
    valid = False
    while not valid:
        car_type = validate_float("""\nWhat type of car do you travel in?:
1) Petrol
2) Diesel
3) Electric
""")

        petrol_emissions = 0.192
        # the average petrol car emits 0.192 kg of co2 per km.
        diesel_emissions = 0.171
        # the average diesel car emits 0.171 kg of co2 per km.
        while car_type in [1, 2, 3]:
            km_per_week = round(validate_float(
                "\nHow many kilometres do you drive per week?: \n"))
            per_year = km_per_week * 52
            print("\nYou drive for", km_per_week, "kilometres per week, "
                  "which is around", per_year, "kilometres per year.")
            # calculate km driven per year
            if car_type == 1:
                # petrol
                # multiply petrol emissions by km per year
                vehicle_emissions = round(per_year * petrol_emissions)

                time.sleep(1)
                print("With a petrol car, you are emitting around",
                      vehicle_emissions, "kilograms of CO2 per year.")
                return vehicle_emissions
            elif car_type == 2:
                # diesel
                # multiply diesel emissions by km per year
                vehicle_emissions = round(per_year * diesel_emissions)
                time.sleep(1)
                print("With a diesel car, you are emitting around",
                      vehicle_emissions, "kilograms of CO2 per year.")
                return vehicle_emissions
            elif car_type == 3:
                # electric
                print("With an electric car, you are emitting no CO2 at all! "
                      "This is great for the environment.")
                vehicle_emissions = 0
                return vehicle_emissions
        else:
            print("Please input a number between 1-3")


# asks user if they know how much electricity they use
# asks user how many people live in their house
# calculates individual electricity usage
def electricity_questions():
    does_user_know_electricity = yes_no(
        "\nDo you know how much electricity you user per month "
        "(if no, we will use the average): ")
    # asks user if they know their electricity usage
    # this is mainly for the younger audience,
    # who don't know their electricity usage
    if does_user_know_electricity == "yes":
        monthly_household_electricity_usage = validate_float(
            "How much electricity does your household "
            "use monthly in kWh (check your electric bill)?: ")
        # asks for monthly household electricity usage
        family_members = validate_float(
            "How many people live in your house?: ")
        # asks for how many people they share the house with
        total_electricity_emissions = individual_electricity_calculator(
            monthly_household_electricity_usage, family_members)
        return total_electricity_emissions
    elif does_user_know_electricity == "no":
        monthly_household_electricity_usage = 909
        # average monthly electricity usage for an individual is 909 kWh
        print("The average electricity usage of individuals in NZ "
              "is 909kWh per month. ")
        time.sleep(1)
        total_electricity_emissions = individual_electricity_calculator(
            monthly_household_electricity_usage, 1)
        return total_electricity_emissions


# tells user their individual electricity usage per month and year
# calculates emissions from electricity usage
def individual_electricity_calculator(monthly_household_electricity_usage,
                                      family_members):
    # divides monthly electricity by family members
    # to find individual electricity usage per month
    individual_electricity = round(
        monthly_household_electricity_usage/family_members)
    print("\nBy yourself, you use around", individual_electricity,
          "kwH of electricity per month.")
    yearly_individual_electricity = individual_electricity * 12
    # multiply by 12 to find electricity usage per year
    time.sleep(2)
    print("This is", yearly_individual_electricity,
          "kwH of electricity per year.")
    electricity_emissions = 0.39
    # 0.39 kg of CO2 per kwH
    total_electricity_emissions = round(
        yearly_individual_electricity * electricity_emissions)
    # multiply by 0.39 to find emissions per year from electricity usage
    return total_electricity_emissions


# asks user if they use LPG gas or not
def gas_yes_no():
    gas_used = yes_no("\nDo you use LPG gas at home?: ")
    # asks user if they use LPG gas as some do not
    if gas_used == "yes":
        co2_from_gas = yearly_gas_used()
        return co2_from_gas
    elif gas_used == "no":
        co2_from_gas = 0
        print("Great! LPG comes from drilling oil and gas wells. "
              "It is a fossil fuel which harms the environment.")
        return co2_from_gas

# asks user what type of gas bottles they used
# calculates total kg of gas used per year
# calculates total CO2 emitted from gas usage per year


# calculates users gas use per year
def yearly_gas_used():
    valid = False
    while not valid:
        gas_type = validate_float("""\nWhat size gas bottles do you use:
1) 9kg LPG bottles
2) 45kg LPG bottles
3) Both?: """)
        # asks user what size gas bottles they use
        if gas_type == 1:
            bottle_size = 9
            # 1kg of lpg gas is 2.95 kg of CO2
            gas_per_month = validate_float(
                "\nHow many bottles do you use per month?: ")
            # asks user how many 9kg bottles they use per month
            total_gas = round(bottle_size * gas_per_month)
            print("\nYou use", total_gas, "kilograms of gas per month")
            yearly_gas = total_gas * 12
            time.sleep(1)
            print("This is", yearly_gas, "kilograms of gas per year")
            co2_from_gas = round(yearly_gas * 2.95)
            return co2_from_gas
        elif gas_type == 2:
            bottle_size = 45
            gas_per_month = validate_float(
                "\nHow many bottles do you use per month?: ")
            # asks user how many 45kg bottles they use per month
            total_gas = round(bottle_size * gas_per_month)
            print("\nYou use", total_gas, "kg of gas per month")
            yearly_gas = total_gas * 12
            time.sleep(1)
            print("This is", yearly_gas, "kg of gas per year")
            co2_from_gas = round(yearly_gas * 2.95)
            return co2_from_gas
        elif gas_type == 3:
            fortyfive_per_month = validate_float(
                "\nHow many 45kg bottles do you use per month?: ")
            # asks user how many 45kg bottles they use per month
            nine_per_month = validate_float(
                "How many 9kg bottles do you use per month?: ")
            # asks user how many 9kg bottles they use per month
            forty_five_bottle_size = 45
            nine_bottle_size = 9
            total_nine_gas = nine_bottle_size * nine_per_month
            total_forty_five_gas = forty_five_bottle_size * fortyfive_per_month
            combined_gas = round(total_forty_five_gas + total_nine_gas)
            print("\nYou use", combined_gas, "kilograms of gas in one month.")
            yearly_combined_gas = combined_gas * 12
            time.sleep(1)
            print("This is", yearly_combined_gas, "kilograms of gas per year.")
            co2_from_gas = round(yearly_combined_gas * 2.95)
            return co2_from_gas
        else:
            print("\nPlease enter a number between 1-3")


# asks user if they have taken any flights this year
def yesno_flights():
    valid = False
    while not valid:
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


def solutions(carbon_footprint):
    time.sleep(1)
    print("\nYour total carbon footprint is", carbon_footprint,
          "kg of CO2 emitted per year.")
    if carbon_footprint < 8600:
        time.sleep(1)
        print(
            "\nAwesome! This is less than the average "
            "carbon footprint in New Zealand, which is 8,600 kg.")
        time.sleep(1)
        print("You can still make some improvements however.")

    elif carbon_footprint > 8600:
        print(
            "\nThis is greater than the average "
            "carbon footprint in New Zealand, which is 8,600kg.")
        print("There are some improvements you can make to "
              "help lower your carbon footprint:")

    improvements = yes_no("Would you like to see these improvements?: ")
    if improvements == "yes":
        print(
            "\nHere are some solutions to help lower "
            "your carbon footprint: ")
        time.sleep(1)
        print("- Use more economic forms of transport, including biking, "
              "walking, electric vehicles and even public transport.")
        time.sleep(1)
        print("- Use less LPG gas.")
        time.sleep(1)
        print("- Plant more trees.")
        time.sleep(1)
        print("- Turn off the water while you brush your teeth.")
        time.sleep(1)
        print("- Use energy efficient products.")
        time.sleep(1)
        print("- Buy second hand or responsibly-made clothes.")
        time.sleep(1)
        print("- Take shorter showers.")
    elif improvements == "no":
        return


# main starts here

use_again = True
while use_again:

    instructions()

    motorcycle_emissions = 0
    train_emissions = 0
    bus_emissions = 0
    total_car_emissions = 0
    # These are all set to 0 except for the user chosen transport.
    # This allows for easier calculations.
    final_vehicle_emissions = main_transport()
    time.sleep(1)
    print("You emit a total of", final_vehicle_emissions,
          "kg of CO2 per year from day-to-day transport.")

    total_electricity_emissions = electricity_questions()
    time.sleep(2)
    print("From electricity usage, you emit", total_electricity_emissions,
          "kg of CO2 per year.")

    co2_from_gas = gas_yes_no()
    time.sleep(1)
    print("This is", co2_from_gas, "kilograms of CO2 per year.")

    total_flight_emissions = yesno_flights()
    time.sleep(1)
    print("From air travel, you have emitted", total_flight_emissions,
          "kilograms of CO2 in the last year.")

    emission_list = [final_vehicle_emissions, total_electricity_emissions,
                     co2_from_gas, total_flight_emissions]
    carbon_footprint = sum(emission_list)
    solutions(carbon_footprint)

    play_again = yes_no("\nWould you like to run the program again?: ")
    if play_again == "yes":
        use_again = True
    elif play_again == "no":
        print("Thank you for using the carbon footprint calculator!")
        use_again = False
