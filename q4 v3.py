import time


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


def individual_electricity_calculator(monthly_household_electricity_usage, family_members):
    individual_electricity_unrounded = monthly_household_electricity_usage/family_members
    # divides monthly electricity by family members to find individual electricity usage per month
    individual_electricity = round(individual_electricity_unrounded)
    print("\nBy yourself, you use around", individual_electricity, "kwH of electricity per month")
    yearly_individual_electricity = individual_electricity * 12
    # multiply by 12 to find electricity usage per year
    time.sleep(2)
    print("\nThis is", yearly_individual_electricity, "kwH of electricity per year")
    electricity_emissions = 0.39
    # 0.39 kg of CO2 per kwH
    total_electricity_emissions_unrounded = yearly_individual_electricity * electricity_emissions
    total_electricity_emissions = round(total_electricity_emissions_unrounded)
    # multiply by 0.39 to find emissions per year from electricity usage
    return total_electricity_emissions


def validate_float(prompt):
    while True:
        try:
            float_input = float(input(prompt))
            return float_input
        except ValueError:
            print("Please input a number ")


def electricity_questions():
    valid = False
    while not valid:
        does_user_know_electricity = yes_no(
            "\nDo you know how much electricity you user per month (if no, we will use the average): ")
        # asks user if they know their electricity usage
        # this is mainly for the younger audience who may not know their electricity usage
        if does_user_know_electricity == "yes":
            monthly_household_electricity_usage = validate_float("\nHow much electricity"
                                                                 " does your household use monthly"
                                                                 " in kWh (check your electric bill)")
            # asks for monthly household electricity usage
            family_members = validate_float("\nHow many people live in your house?: ")
            # asks for how many people they share the house with
            total_electricity_emissions = individual_electricity_calculator(monthly_household_electricity_usage,
                                                                            family_members)
            return total_electricity_emissions
        elif does_user_know_electricity == "no":
            monthly_household_electricity_usage = 909
            # average monthly electricity usage for an individual is 909 kWh
            print("\nThe average electricity usage of individuals in NZ is 909kWh per month. ")
            total_electricity_emissions = individual_electricity_calculator(monthly_household_electricity_usage, 1)
            return total_electricity_emissions

# main goes here


total_electricity_emissions = electricity_questions()
time.sleep(2)
print("\nFrom electricity usage, you emit", total_electricity_emissions, "kg of CO2 per year.")
