valid = False
while not valid:
    do_you_recycle = input("Do you recycle?")
    if do_you_recycle == "yes":
        print("good")
        break
    if do_you_recycle == "no":
        print("bad")
        break
    else:
        print("\nplease input yes or no")

    # clean_energy = input("do you use clean energy such as solar or wind?: ")