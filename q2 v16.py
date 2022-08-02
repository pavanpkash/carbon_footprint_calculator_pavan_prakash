import time

# Functions go here


def validate_float(prompt):
    while True:
        try:
            float_input = float(input(prompt))
            return float_input
        except ValueError:
            print("Please input a number: ")


# This function asks the user what their main form of transport is
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
            # asks user whether they drive a petrol, diesel or electric car
            vehicle_emissions = petrol_diesel_emissions()
            # when the user selects this transport, every other transport will = 0 for easy calculations
            # this applies for every selectable transport
            return vehicle_emissions

        elif transport == 2:
            # bus
            how_often = validate_float("\nHow many times a week do you use the bus? "
                                       "(if once per day type 7, if twice a day type 14): ")
            # if the user uses a bus, they will be asked how often they use the bus
            km_per_ride = validate_float("\nRoughly how many kilometres is one bus ride.")
            bus_per_year_unrounded = how_often * 52 * km_per_ride
            bus_per_year = round(bus_per_year_unrounded)
            # will then figure out how many times per year they use the bus
            print("\nYou travel around", bus_per_year, "kilometers per year in a bus.")
            vehicle_emissions_unrounded = bus_per_year * 0.105
            vehicle_emissions = round(vehicle_emissions_unrounded)
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
            how_often = validate_float("\nHow many times a week do you use the train? "
                                       "(if once per day type 7, if twice a day type 14): ")
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

        elif transport == 6:
            # motorcycle
            km_per_week_unrounded = validate_float("\nHow many kilometres do you ride per week?: \n")
            km_per_week = round(km_per_week_unrounded)
            per_year = km_per_week * 52
            print("\nYou drive for", km_per_week, "kilometres per week, "
                                                  "which is around", per_year, "kilometres per year.")
            vehicle_emissions_unrounded = per_year * 0.103
            vehicle_emissions = round(vehicle_emissions_unrounded)
            # motorcycle emissions = 0.103kg/km
            return vehicle_emissions
        else:
            print("Please input 1, 2, 3, 4, 5 or 6: ")
    # if the transport is one of the listed options, it will use the final_vehicle_emission_calculator function


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
            km_per_week_unrounded = validate_float("\nHow many kilometres do you drive per week?: \n")
            km_per_week = round(km_per_week_unrounded)
            per_year = km_per_week * 52
            print("\nYou drive for", km_per_week, "kilometres per week, "
                                                  "which is around", per_year, "kilometres per year.")
            # calculate km driven per year
            if car_type == 1:
                # petrol
                vehicle_emissions_unrounded = per_year * petrol_emissions
                # multiply petrol emissions by km per year
                vehicle_emissions = round(vehicle_emissions_unrounded)
                # round is used throughout the program to give an appealing round number with no dp
                time.sleep(1)
                print("With a petrol car, you are emitting around", vehicle_emissions, "kilograms of CO2 per year.")
                return vehicle_emissions
            elif car_type == 2:
                # diesel
                vehicle_emissions_unrounded = per_year * diesel_emissions
                # multiply diesel emissions by km per year
                vehicle_emissions = round(vehicle_emissions_unrounded)
                time.sleep(1)
                print("With a diesel car, you are emitting around", vehicle_emissions, "kilograms of CO2 per year.")
                return vehicle_emissions
            elif car_type == 3:
                # electric
                print("With an electric car, you are emitting no CO2 at all! This is great for the environment.")
                vehicle_emissions = 0
                return vehicle_emissions
        else:
            print("Please input 1-3")

# main starts here

motorcycle_emissions = 0
train_emissions = 0
bus_emissions = 0
total_car_emissions = 0
# These are all set to 0 except for the user chosen transport which will change this amount.
# This allows for easier calculations.
final_vehicle_emissions = main_transport()
time.sleep(1)
print("You emit a total of", final_vehicle_emissions, "kg of CO2 per year from day-to-day transport.")
