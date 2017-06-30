from user_name import *
from user_age import *
from user_rating import *
friends ={
    'name':["Vineet"],
    'age':["20"],
    'rating':["A great spy"]
    }
def add_friend():
    add_name = ask_name()
    add_age = ask_age()
    add_rating = ask_rating()
    friends['name'].append(add_name)
    friends['age'].append(add_age)
    friends['rating'].append(add_rating)
    # print(friends)
# add_friend()

def select_a_friend():
    for (index,name) in enumerate(friends['name']):
        print (index + 1,name, friends['age'][index],friends['rating'][index])
        status_choice = int(raw_input("Choose a friend: "))
        return status_choice
        # print friends['name'][status_choice-1],friends['age'][status_choice-1],friends['rating'][status_choice-1]
# select_a_friend()



