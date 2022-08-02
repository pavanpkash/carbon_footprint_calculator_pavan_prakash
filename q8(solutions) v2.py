import time

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


final_vehicle_emissions = 1
total_electricity_emissions = 1
co2_from_gas = 1
total_flight_emissions = 1

# starts here

emission_list = [final_vehicle_emissions, total_electricity_emissions,
                 co2_from_gas, total_flight_emissions]
carbon_footprint = sum(emission_list)
solutions(carbon_footprint)
