def ask_status():
    spy_status = (raw_input('enter your status : '))
    if len(spy_status) == 0:
        print ("please input information")
        ask_status()

    elif spy_status.isalpha() == False:
        print ("please input valid information")
        ask_status()
    elif spy_status.lower() == 'online':
        return ('Spy is online ')
    elif spy_status.lower() == "offline":
        return ('Spy is offline')

    else:
        print ("please enter online/offline:")
        ask_status()


