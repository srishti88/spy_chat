status = ["we are one","i am busy","see you"]

def display_status():
    for (index,stat) in enumerate(status):
        print (index+1 ,status[index])
    status_choice = int(raw_input("Choose a status: "))
    print ("Status choosen by you is:-%s ") %(status[status_choice-1])
    return status[status_choice-1]


def update_status():
    status_input = raw_input("Please enter a status: ")
    status.append(status_input)
    print ("Your status '%s")% status[len(status)-1]
def ask_status():
    status_choice = raw_input("do you want to choose from default status : Y/N ")
    if status_choice.upper() == 'Y':
        return display_status()
    else:
        # print "O "
        print update_status()
# ask_status()

