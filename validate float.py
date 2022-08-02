# This function makes sure the user has entered a number
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


# main
validate_float("prompt")
