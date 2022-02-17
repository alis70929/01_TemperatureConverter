def temp_check(low):
    valid = False
    while not valid:
        try:
            response = float(input("Enter a Number"))

            if response < low:
                print("too cold")
            else:
                return response

        except ValueError:
            print("Please Enter a number")
