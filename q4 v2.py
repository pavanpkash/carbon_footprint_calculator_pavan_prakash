def electricity(monthly_household_electricity_usage, family_members):
    individual_electricity_unrounded = monthly_household_electricity_usage/family_members
    individual_electricity = round(individual_electricity_unrounded)
    print("\nBy yourself, you use around", individual_electricity, "kwH of electricity per month")
    yearly_individual_electricity = individual_electricity * 12
    print("This is", yearly_individual_electricity, "kwH of electricity per year")
    electricity_emissions = 0.39
    # 0.39 kg of CO2 per kwH
    total_electricity_emissions_unrounded = yearly_individual_electricity * electricity_emissions
    total_electricity_emissions = round(total_electricity_emissions_unrounded)
    return total_electricity_emissions


def validate_float(prompt):
    while True:
        try:
            float_input = float(input(prompt))
            return float_input
        except ValueError:
            print("Please input a number ")

# main goes here
valid = False
while not valid:
    does_user_know_electricity = input("\nDo you know how much electricity you user per month (if no, we will use the average): ")
    if does_user_know_electricity == "yes":
        monthly_household_electricity_usage = int(input("How much electricity does your household use monthly in kWh (check your electric bill)"))
        family_members = int(input("How many people live in your house?: "))
        total_electricity_emissions = electricity(monthly_household_electricity_usage, family_members)
        print("From electricity usage, you emit", total_electricity_emissions, "kg of CO2 per year.")
        break
    elif does_user_know_electricity == "no":
        monthly_household_electricity_usage = 909
        print("\nThe average electricity usage of individuals in NZ is 909kWh per month. ")
        total_electricity_emissions = electricity(monthly_household_electricity_usage, 1)
        print("From electricity usage, you emit", total_electricity_emissions, "kg of CO2 per year.")
        break
    else:
        print("\nPlease input yes or no: ")