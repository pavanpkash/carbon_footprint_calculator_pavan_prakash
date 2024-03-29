# defs go here
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
                how_often = int(input("""\nHow many times a week do you use the bus? (if once per day type 7, if twice a day type 14)\n"""))
                km_per_ride = int(input("\nRoughly how many kilometres is one bus ride"))
                bus_per_year = how_often * 52 * km_per_ride
                print("You travel around", bus_per_year, "kilometers per year in a bus")
                bus_emissions = bus_per_year * 105
                # user_emissions = bus_emissions / 20 - don't need this as value is per passenger
                # there is an average of around 20 people on a bus when travelling to and from work or school, so I have divided the emissions among the passengers
                print("you emit", bus_emissions, "per year")
                # emissions = 822gm / km
                return bus_emissions
            elif transport == "train":
                how_often = int(input("""\nHow many times a week do you use the train? (if once per day type 7, if twice a day type 14)\n"""))
                km_per_ride = int(input("Roughly how many kilometres is one train ride"))
                train_per_year = how_often * 52 * km_per_ride
                print("You travel around", train_per_year, "kilometers per year in a bus")
                train_emissions = train_per_year * 41
                # emissions = 41gm/km
                # user_emissions = train_emissions / 20  - don't need this as value is per passenger
                print("you emit", train_emissions, "per year")
                return train_emissions
        except ValueError:
            print("Please enter a number")

def q2(car_type):
    valid = False
    while not valid:
        try:
            while car_type in ["diesel", "electric", "petrol"]:
                km_per_week = int(input("\nhow many kilometres do you drive per week?\n"))
                #use km per week instead of minutes for easy calculations
                per_year = km_per_week * 52
                print("\nyou drive for", km_per_week, "kilometres per week, which is around", per_year, "kilometres per year")
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
        print("with a petrol car, you are emitting around" , total_emissions, "grams of CO2 per year. This is", total_emissions_in_tonnes, "tonnes of CO2 per year.")
        return total_emissions
    elif car_type == "diesel":
        total_emissions = per_year * diesel_emissions
        total_emissions_in_kg = total_emissions / 1000
        total_emissions_in_tonnes = total_emissions_in_kg / 1000
        print("with a diesel car, you are emitting around" , total_emissions, "grams of CO2 per year. This is", total_emissions_in_tonnes, "tonnes of CO2 per year.")
        return total_emissions
    elif car_type == "electric":
        print("with an electric car, you are emitting no CO2 at all! This is great for the environment")

def electricity(monthly_household_electricity_usage, family_members):
    individual_electricity = monthly_household_electricity_usage / family_members
    print("\nBy yourself, you use around", individual_electricity, "kwH of electricity per month")
    yearly_individual_electricity = individual_electricity * 12
    print("This is", yearly_individual_electricity, "kwH of electricity per year")

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

# main goes here
valid = False
while not valid:
    does_user_know_electricity = input(
        "\nDo you know how much electricity you user per month (if no, we will use the average): ")
    if does_user_know_electricity == "yes":
        print("\ncool")
        monthly_household_electricity_usage = int(
            input("how much electricity does your household use monthly in kWh (check your electric bill)"))
        family_members = int(input("how many people live in your house?"))
        electricity(monthly_household_electricity_usage, family_members)
        break
    elif does_user_know_electricity == "no":
        monthly_household_electricity_usage = 909
        print("\nThe average electricity usage of individuals in NZ is 909kWh per month")
        electricity(monthly_household_electricity_usage, 1)
        break
    else:
        print("\nplease input yes or no")

    # clean_energy = input("do you use clean energy such as solar or wind?: ")

# user inputs kwh from electric bill
# divide by people in the house
# = average electricity for just them

# add a run again feature