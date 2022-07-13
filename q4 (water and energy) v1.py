def electricity(monthly_household_electricity_usage, family_members):
    individual_electricity = monthly_household_electricity_usage/family_members
    print("\nBy yourself, you use around", individual_electricity,"kwH of electricity per month")
    yearly_individual_electricity = individual_electricity * 12
    print("This is", yearly_individual_electricity, "kwH of electricity per year")

# main goes here
valid = False
while not valid:
    does_user_know_electricity = input("\nDo you know how much electricity you user per month (if no, we will use the average): ")
    if does_user_know_electricity == "yes":
        print("\ncool")
        monthly_household_electricity_usage = int(input("how much electricity does your household use monthly in kWh (check your electric bill)"))
        family_members = int(input("how many people live in your house?"))
        electricity(monthly_household_electricity_usage, family_members)
        break
    elif does_user_know_electricity == "no":
        monthly_household_electricity_usage = 909
        print("\nThe average electricity usage of individuals in NZ is 909kWh per month")
        electricity(monthly_household_electricity_usage, 1)
        break
    else:
        print("\nplease input yes or no")

    # clean_energy = input("do you use clean energy such as solar or wind?: ")

#user inputs kwh from electric bill
#divide by people in the house
#= average electricity for just them