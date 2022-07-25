use_again = True
while use_again:


    play_again = yes_no("Would you like to run the program again?: ")
    if play_again == "yes":
        use_again = True
    elif play_again == "no":
        use_again = False