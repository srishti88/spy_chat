from user_name import ask_name,ask_salutation

from spy_details import * #imported files
from message import *
from friends import *
from menu import *
from user_age import *
from user_rating import *
from user_status import *
def start_chat():  #begenning of the programme
    default = raw_input("Do you want to continue as a default user. Y/N: ")
    if default.upper() == "Y":
        spy_salutation = default_user.salutation
        spy_name = default_user.name
        spy_age = default_user.age
        spy_rating = default_user.rating
        spy_status = default_user.status
        spy_details  = [spy_salutation,spy_name,spy_age,spy_rating,spy_status]
        return spy_details
    elif default.upper() == "N":
        spy_salutation = str(ask_salutation())
        spy_name = str(ask_name())
        spy_age = str(ask_age())
        spy_rating = str(ask_rating())
        spy_status = str(ask_status())
        spy_details = [spy_salutation, spy_name, spy_age, spy_rating, spy_status]
        # spy_details = [ask_name(),ask_salutation(),ask_age(),ask_rating(),ask_status()]
        return spy_details
    else:
        print "Not a valid option"
        start_chat()

# to display details of spy
def display(spy_details):
    print("Welcome " + spy_details[0] + spy_details[1] + " you are " + spy_details[2] + " years old " + " you are rated as " + spy_details[3] + "and your current status is " + spy_details[4])
display(start_chat())
user_choice = menu()
if user_choice == 1:
    ask_status()
elif user_choice == 2:
    add_friend()
elif user_choice ==3:
    encrypt_message()
elif user_choice == 4:
    decrypt_message()
elif user_choice == 5:
    read_chat_history()
else:
    exit(0)
