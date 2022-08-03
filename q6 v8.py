import time


def validate_float(prompt):
    while True:
        try:
            float_input = float(input(prompt))
            if float_input > 0:
                return float_input
            elif float_input <= 0:
                print("Please input a number greater than 0")
                # user must input a number greater than 0
        except ValueError:
            print("Please input a number ")
            # user must input a number


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
            # 1kg of lpg gas is 2.95 kg of CO2
            bottle_size = 9
            co2_from_gas = monthly_gas(bottle_size)
            return co2_from_gas
        elif gas_type == 2:
            bottle_size = 45
            co2_from_gas = monthly_gas(bottle_size)
            return co2_from_gas
        elif gas_type == 3:
            fortyfive_per_month = validate_float(
                "\nHow many 45kg bottles do you use per month?: ")
            # asks user how many 45kg bottles they use per month
            nine_per_month = validate_float(
                "How many 9kg bottles do you use per month?: ")
            # asks user how many 9kg bottles they use per month
            total_nine_gas = 9 * nine_per_month
            total_forty_five_gas = 45 * fortyfive_per_month
            total_gas = round(total_forty_five_gas + total_nine_gas)
            co2_from_gas = gas_calculator(total_gas)
            return co2_from_gas
        else:
            print("\nPlease enter one of these")


def monthly_gas(bottle_size):
    gas_per_month = validate_float(
        "\nHow many bottles do you use per month?: ")
    # asks user how many 45kg bottles they use per month
    total_gas = round(bottle_size * gas_per_month)
    co2_from_gas = gas_calculator(total_gas)
    return co2_from_gas

def gas_calculator(total_gas):
    print("\nYou use", total_gas, "kg of gas per month")
    yearly_gas = total_gas * 12
    time.sleep(1)
    print("This is", yearly_gas, "kg of gas per year")
    co2_from_gas = round(yearly_gas * 2.95)
    return co2_from_gas

# main starts here

co2_from_gas = gas_yes_no()
time.sleep(1)
print("This is", co2_from_gas, "kilograms of CO2 per year.")
