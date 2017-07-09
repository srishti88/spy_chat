def menu():

    print ("1.Add a status update")
    print ("2.Add a friend")
    print("3.Send a secert message")
    print ("3.Read a secert message")
    print ("4.Read chats from the user")
    print ("5.Close application")
    user_choice = raw_input("Please select option: ")
    if len(user_choice) > 0:
        user_choice = int (user_choice)
        return user_choice




