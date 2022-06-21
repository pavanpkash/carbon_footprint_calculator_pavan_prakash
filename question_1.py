def question_1():
    transport = input("""What is your main form of transport?:
- Car
- Bus
- Walk
- Bike
""")
    if transport == "car":
        car_type = input("""what type of car do you travel in?
- Petrol
- Diesel
- Electric
""")
        if car_type == "petrol":
            print("petrol")
        elif car_type == "diesel":
            
            print("diesel")
        elif car_type == "electric":
            print("electric")
        else:
            print("please input petrol, diesel or electric")
    elif transport == "bus":
        how_often = input("""How often do you use the bus?
- Everyday
- Occasionally
""")
    elif transport == "walk":
        print(")
    elif transport == "bike":
        print("Nice! You're already helping the environment")

question_1()

if usertransport == "car":
    print("test")