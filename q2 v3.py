def question_1(transport):
    valid = False
    while not valid:
        try:
            if transport == "car":
                car_type = input("""\nwhat type of car do you travel in?
- Petrol
- Diesel
- Electric
""")
                if car_type in ["petrol", "diesel", "electric"]:
                    return car_type
                else:
                    print("please input petrol, diesel or electric")
            elif transport == "bus":
                how_often = input("""How often do you use the bus?
- Everyday
- Occasionally (if once per month type 1m, if once per year type 1y)
""")
                return how_often
        except ValueError:
            print("no")

def q2(car_type):
    if car_type in ["diesel", "electric", "petrol"]:
        how_often = input("""\nhow often do you drive or get driven?
- Everyday
- Once a week
- Once a month
- Other """)
        if how_often == "everyday":
            per_day = int(input("how many minutes a day? "))
            print("you drive for", per_day, "minutes per day")
            return per_day
        elif how_often ==

#main starts here
valid = False
while not valid:
    transport = input("""What is your main form of transport?:
    - Car
    - Bus
    - Walk
    - Bike
    """)
    if transport == "car":
        car_type = question_1(transport)
        per_day = q2(car_type)
        break
    elif transport == "bus":
        print("bus")
        break
    elif transport in ["bike", "walk"]:
        print("Nice, you're already helping the environment!")
        break
    else:
        print("try again")