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
            elif transport == "walk":
                print("walk")
            elif transport == "bike":
                print("Nice! You're already helping the environment")
                return
        except ValueError:
            print("no")

def q2(car_type):
    if car_type in ["diesel", "electric", "petrol"]:
        how_often = input("""\nhow often do you drive or get driven?
- Everyday
- Once a week
- Once a month in ["bike", "walk"]:
    print("gay")
else:
    print("please enter one of these")

#solution
print("""Your car type is""",x,""".
This means that""")
per_day = q2(x)
