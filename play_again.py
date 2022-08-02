use_again = True
while use_again:


    play_again = yes_no("\nWould you like to run the program again?: ")
    if play_again == "yes":
        use_again = True
    elif play_again == "no":
        print("Thank you for using the carbon footprint calculator!")
        use_again = False