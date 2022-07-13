def gas():
    valid = False
    while not valid:
        try:
            gas_type = input("""\nwhat size gas bottles do you use:
- 9kg LPG bottles
- 45kg LPG bottles
- Both?: """).lower()
            if gas_type in ["9", "9kg"]:
                bottle_size = 9
                gas_per_month = int(input("\nhow many bottles do you use per month?"))
                print(gas_per_month)
                total_gas = bottle_size * gas_per_month
                print("you use", total_gas, "kg of gas per month")
                break
            elif gas_type in ["45", "45kg"]:
                bottle_size = 45
                gas_per_month = int(input("\nhow many bottles do you use per month?"))
                print(gas_per_month)
                total_gas = bottle_size * gas_per_month
                print("you use", total_gas, "kg of gas per month")
                yearly_gas = total_gas * 12
                print("this is", yearly_gas, "kg of gas per year")
                break
            else:
                print("please enter one of these")
            print(gas_type)
        except ValueError:
            print("no")


# main starts here
valid = False
while not valid:
    gas_used = input("Do you use LPG gas at home?: ").lower()
    if gas_used == "yes":
        gas()
        break
    if gas_used == "no":
        break
    else:
        print("\nplease input yes or no")
