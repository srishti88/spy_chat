def ask_name():
    spy_name = raw_input("Enter your Name")
    if len(spy_name) > 0:
        if spy_name.isalpha(): #str.isalpha(spy_name)
            return str(spy_name)
        else:
            print  ("Please enter a String Value")
            ask_name()
    else:
        print  ("Name can not be empty")
        ask_name()



def ask_salutation():
    spy_salutation = raw_input("enter your salutation.MR/MISS: ")
    if spy_salutation.upper() == "MR":
        return ("Mr")

    elif spy_salutation.upper() == "MISS":
        return ("Miss")
    else:
        print  "Not a valid option"
        ask_salutation()




