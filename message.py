import sys
from termcolor import colored, cprint
from friends import *
from datetime import datetime
from steganography.steganography import Steganography
#using steganography library to encrypt
def encrypt_message():
    input_image = raw_input("please select an image to encode: ")
    input_message = raw_input("please enter a message you would like to encrypt: ")
    friend.chat.append(input_message + " " + str(datetime.now()))
    out_image = raw_input("plese enter the specific name of the encoded image : ")
    Steganography.encode(input_image,out_image,input_message)
    output = "message encoded"
    print output
# encrypt_message()
#stegnography to decrypt message
def decrypt_message():
    image_path = raw_input("please select a image to decode : ")
    try:    #used exception handaling
        decrypted_message = Steganography.decode(image_path)
        text = colored(decrypted_message, 'black')
        print text
        if len(decrypted_message) > 100:
            exit(0)
        else:
            number_of_words = len(decrypted_message)
            if "SOS" in decrypted_message.upper():
                print("Save our souls")
            elif "SAVE ME" in decrypted_message.upper():
                print("need immediate help")
                return decrypted_message
    except:
        print("image doesnot contain any secert message")

def send_message():
    friend_choice =int( select_a_friend())
    print ("your message has been successfully send to %s ")%(friends['name'][friend_choice -1])
def read_chat_history():
    read_for = select_a_friend()


    for chat in friend.chat:
        print ("Your message is : " + chat)
        print (colored(friend.name,'red'),colored(chat,'black'),colored(datetime,'blue'))




