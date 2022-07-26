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

def gas():
    valid = False
    while not valid:
        try:
            gas_type = input("""\nWhat size gas bottles do you use:
- 9kg LPG bottles
- 45kg LPG bottles
- Both?: """).lower()
            if gas_type in ["9", "9kg"]:
                bottle_size = 9
                # 1kg of lpg gas is 2.95 kg of CO2
                gas_per_month = validate_float("\nHow many bottles do you use per month?")
                total_gas_unrounded = bottle_size * gas_per_month
                total_gas = round(total_gas_unrounded)
                print("You use", total_gas, "kilograms of gas per month")
                yearly_gas = total_gas * 12
                print("This is", yearly_gas, "kilograms of gas per year")
                co2_from_gas_unrounded = yearly_gas * 2.95
                co2_from_gas = round(co2_from_gas_unrounded)
                return co2_from_gas
            elif gas_type in ["45", "45kg"]:
                bottle_size = 45
                gas_per_month = validate_float("\nHow many bottles do you use per month?")
                total_gas_unrounded = bottle_size * gas_per_month
                total_gas = round(total_gas_unrounded)
                print("You use", total_gas, "kg of gas per month")
                yearly_gas = total_gas * 12
                print("This is", yearly_gas, "kg of gas per year")
                co2_from_gas_unrounded = yearly_gas * 2.95
                co2_from_gas = round(co2_from_gas_unrounded)
                return co2_from_gas
            elif gas_type in ["both", "b"]:
                fortyfive_per_month = validate_float("\nHow many 45kg bottles do you use per month?: ")
                nine_per_month = validate_float("\nHow many 9kg bottles do you use per month?: ")
                fortyfive_bottle_size = 45
                nine_bottle_size = 9
                total_nine_gas = nine_bottle_size * nine_per_month
                total_fortyfive_gas = fortyfive_bottle_size * fortyfive_per_month
                combined_gas_unrounded = total_fortyfive_gas + total_nine_gas
                combined_gas = round(combined_gas_unrounded)
                print("\nYou use", combined_gas, "kilograms of gas in one month.")
                yearly_combined_gas = combined_gas * 12
                print("This is", yearly_combined_gas, "kilograms of gas per year.")
                co2_from_gas_unrounded = yearly_combined_gas * 2.95
                co2_from_gas = round(co2_from_gas_unrounded)
                return co2_from_gas
            else:
                print("\nPlease enter one of these")
            print(gas_type)
        except ValueError:
            print("no")

def validate_float(prompt):
    while True:
        try:
            float_input = float(input(prompt))
            return float_input
        except ValueError:
            print("Please input a number ")

def gas_yes_no():
    valid = False
    while not valid:
        gas_used = yes_no("Do you use LPG gas at home?: ")
        if gas_used == "yes":
            gas()
            break
        elif gas_used == "no":
            break

# main starts here

co2_from_gas = gas_yes_no()