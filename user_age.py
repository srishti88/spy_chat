def ask_age():
    spy_age = (raw_input('enter your age'))
    if len(spy_age) == 0:
        print ("please input information")
        ask_age()

    elif spy_age.isdigit() == False:
        print ("please input valid information")
        ask_age()
    elif int(spy_age) >12 and int(spy_age) < 50:
        return spy_age
    else:
        print ("you are not eligible")
        ask_age()
