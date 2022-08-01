import time

# Functions go here


def validate_float(prompt):
    while True:
        try:
            float_input = float(input(prompt))
            return float_input
        except ValueError:
            print("Please input a number: ")


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

# main starts here


motorcycle_emissions = 0
train_emissions = 0
bus_emissions = 0
total_car_emissions = 0
final_vehicle_emissions = total_vehicle_emission_calculator()
time.sleep(1)
print("You emit a total of", final_vehicle_emissions, "kg of CO2 per year from day-to-day transport.")
