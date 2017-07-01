def ask_rating():
    spy_rating = (raw_input('enter spy rating in float'))
    if len(spy_rating) == 0:
        return ("please input information")
        ask_rating()

    else:
        try: #using exception handaling
            spy_rating = float(spy_rating)
            if spy_rating > 5 :
                print ("A spy can not have a rating more than 5")
                spy_rating()
            elif spy_rating >= 4 and spy_rating <5:
                return (" a great spy ")
            elif spy_rating >=3 and spy_rating <4:
                return (" a good spy")
            elif spy_rating>=2 and spy_rating < 3:
                return (" a average spy")
            elif spy_rating >=1 and spy_rating < 2:
                return (" a below average view ")
            else:
                print("Please enter a valid option")

                spy_rating()
        except:
            ask_rating()
