def question_1(transport):
    if transport == "car":
        car_type = input("""what type of car do you travel in?
    - Petrol
    - Diesel
    - Electric
    """)
        if car_type == "petrol":
            return car_type
        elif car_type == "diesel":
            return car_type
        elif car_type == "electric":
            return car_type
        else:
            print("please input petrol, diesel or electric")
    if transport == "bus":
        how_often = input("""How often do you use the bus?
    - Everyday
    - Occasionally
    """)
    elif transport == "walk":
        print("walk")
    elif transport == "bike":
        print("Nice! You're already helping the environment")

#main starts here
transport = input("""What is your main form of transport?:
- Car
- Bus
- Walk
- Bike
""")

car_type = question_1(transport)
#solution

print("your car type is ", car_type)

