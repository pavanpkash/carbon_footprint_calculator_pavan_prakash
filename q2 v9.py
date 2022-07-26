# Functions go here

def main_transport(transport):
    # this function asks the user what their main form of transport is
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
                how_often = validate_float("""\nHow many times a week do you use the bus? (if once per day type 7, if twice a day type 14): \n""")
                km_per_ride = validate_float("\nRoughly how many kilometres is one bus ride.")
                bus_per_year_unrounded = how_often * 52 * km_per_ride
                bus_per_year = round(bus_per_year_unrounded)
                print("You travel around", bus_per_year, "kilometers per year in a bus.")
                bus_emissions_unrounded = bus_per_year * 0.105
                bus_emissions = round(bus_emissions_unrounded)
                # user_emissions = bus_emissions / 20 - don't need this as value is per passenger
                # there is an average of around 20 people on a bus when travelling to and from work or school, so I have divided the emissions among the passengers
                print("You emit", bus_emissions, "kilograms of CO2 per year.")
                # bus emissions = 0.105kg / km
                return bus_emissions
            elif transport == "train":
                how_often = validate_float("""\nHow many times a week do you use the train? (if once per day type 7, if twice a day type 14):\n""")
                km_per_ride = validate_float("Roughly how many kilometres is one train ride?: ")
                train_per_year_unrounded = how_often * 52 * km_per_ride
                train_per_year = round(train_per_year_unrounded)
                print("You travel around", train_per_year, "kilometers per year in a bus.")
                train_emissions_unrounded = train_per_year * 0.041
                train_emissions = round(train_emissions_unrounded)
                # emissions = 0.041kg/km
                # user_emissions = train_emissions / 20  - don't need this as value is per passenger
                print("By travelling on train, you emit", train_emissions, "kilograms of CO2 per year.")
                return train_emissions
            elif transport == "motorcycle":
                km_per_week_unrounded = validate_float("\nHow many kilometres do you drive per week?: \n")
                km_per_week = round(km_per_week_unrounded)

        except ValueError:
            print("Please enter a number: ")

def fuel(car_type):
    valid = False
    while not valid:
        try:
            while car_type in ["diesel", "electric", "petrol"]:
                km_per_week_unrounded = validate_float("\nHow many kilometres do you drive per week?: \n")
                km_per_week = round(km_per_week_unrounded)
                #use km per week instead of minutes for easy calculations
                per_year = km_per_week * 52
                print("\nYou drive for", km_per_week, "kilometres per week, which is around", per_year, "kilometres per year.")
                return per_year
        except ValueError:
            print("Please enter a number: ")

def q3(car_type, per_year):
    petrol_emissions = 192
    #the average petrol car emits 192 grams of co2 per km.
    diesel_emissions = 171
    #the average diesel car emits 171 grams of co2 per km.
    if car_type == "petrol":
        total_car_emissions_unrounded = per_year * petrol_emissions
        total_car_emissions = round(total_car_emissions_unrounded)
        total_car_emissions_in_kg_unrounded = total_car_emissions/1000
        total_car_emissions_in_kg = round(total_car_emissions_in_kg_unrounded)
        total_car_emissions_in_tonnes_unrounded = total_car_emissions_in_kg/1000
        total_car_emissions_in_tonnes = round(total_car_emissions_in_tonnes_unrounded)
        print("With a petrol car, you are emitting around", total_car_emissions_in_kg, "kilograms of CO2 per year. This is", total_car_emissions_in_tonnes, "tonnes of CO2 per year.")
        return total_car_emissions_in_kg
    elif car_type == "diesel":
        total_car_emissions_unrounded = per_year * diesel_emissions
        total_car_emissions = round(total_car_emissions_unrounded)
        total_car_emissions_in_kg = total_car_emissions / 1000
        total_car_emissions_in_tonnes_unrounded = total_car_emissions_in_kg / 1000
        total_car_emissions_in_tonnes = round(total_car_emissions_in_tonnes_unrounded)
        print("With a diesel car, you are emitting around", total_car_emissions_in_kg, "kilograms of CO2 per year. This is", total_car_emissions_in_tonnes, "tonnes of CO2 per year.")
        return total_car_emissions_in_kg
    elif car_type == "electric":
        print("With an electric car, you are emitting no CO2 at all! This is great for the environment.")

def validate_float(prompt):
    while True:
        try:
            float_input = float(input(prompt))
            return float_input
        except ValueError:
            print("Please input a number: ")

def newdef(transport):
    if transport == "car":
        # should accept upper case or lower
        car_type = main_transport(transport)
        per_year = fuel(car_type)
        total_car_emissions_in_kg = q3(car_type, per_year)
        bus_emissions = 0
        train_emissions = 0
        return total_car_emissions_in_kg, bus_emissions, train_emissions

    elif transport == "bus":
        bus_emissions = main_transport(transport)
        train_emissions = 0
        total_car_emissions_in_kg = 0
        return bus_emissions, train_emissions, total_car_emissions_in_kg

    elif transport in ["bike", "walk"]:
        print("Nice, you're already helping the environment!")
        return

    elif transport == "train":
        train_emissions = main_transport(transport)
        bus_emissions = main_transport(transport)
        total_car_emissions_in_kg = 0
        return train_emissions, bus_emissions, total_car_emissions_in_kg
    else:
        print("Please input car, bus, walk, bike, train or motorcycle: ")

#main starts here
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
    if transport in ["car", "bus", "train", "walk", "bike", "motorcycle"]:
        bus_emissions, train_emissions, total_car_emissions_in_kg = newdef(transport)
        final_vehicle_emissions = bus_emissions + train_emissions + total_car_emissions_in_kg
        print("You emit a total of", final_vehicle_emissions, "kg of CO2 from vehicular travel")
        break
    else:
        print("Please enter a valid value")