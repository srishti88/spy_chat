from user_name import *#imported files
from user_age import *
from user_rating import *
#  using classes
class friends:
    def __init__(self,name,age,rating,chat) :
        self.name = name
        self.age = age
        self.rating = rating
        self.chat = chat
friend = friends('vineet','20','a great spy','hello')
def add_friend():
    add_name = ask_name()
    add_age = ask_age()
    add_rating = ask_rating()
    friend.name.append(add_name)
    friend.age.append(add_age)
    friend.rating.append(add_rating)
    # print(friends)
# add_friend()
#selecting a friend by using index
def select_a_friend():
    for (index,name) in enumerate(friend.name):
        print (index + 1,friend.name, friend.age,friend.rating)
        status_choice = int(raw_input("Choose a friend: "))
        return status_choice
        # print friends['name'][status_choice-1],friends['age'][status_choice-1],friends['rating'][status_choice-1]
# select_a_friend()



