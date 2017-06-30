from user_name import ask_name,ask_salutation
from spy_details import *
from user_age import *
from user_rating import *
from user_status import *
def start_chat():
    default = raw_input("Do you want to continue as a default user. Y/N: ")
    if default.upper() == "Y":
        spy_salutation = default_user['salutation']
        spy_name = default_user['name']
        spy_age = default_user['age']
        spy_rating = default_user['rating']
        spy_status = default_user['status']
        spy_details  = [spy_salutation,spy_name,spy_age,spy_rating,spy_status]
        return spy_details
    elif default.upper() == "N":
        spy_details = [ask_name(),ask_salutation(),ask_age(),ask_rating(),ask_status()]
        return spy_details
    else:
        print "Not a valid option"
        start_chat()

def display(spy_details):
    print("Welcome " + spy_details[0] + spy_details[1] + " you are " + spy_details[2] + " years old " + " you are rated as " + spy_details[3])

display(start_chat())

