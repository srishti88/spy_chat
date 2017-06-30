from friends import *
from steganography.steganography import Steganography
def encrypt_message():
    input_image = raw_input("please select an image to encode: ")
    input_message = raw_input("please enter a message you would like to encrypt: ")
    out_image = raw_input("plese enter the specific name of the encoded image : ")
    Steganography.encode(input_image,out_image,input_message)
    output = "message encoded"
    return output
# encrypt_message()

def send_message():
    friend_choice =int( select_a_friend())
    print ("your message has been successfully send to %s ")%(friends['name'][friend_choice -1])
send_message()