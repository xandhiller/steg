from PIL import Image
# import os

io = 'jim.jpg'

class text:
    def __init__:
        
class image:
    def __init__:


# String to binary array
def string_to_binary(string):
    serial = []
    for character in string:
        #serial.append(bin(ord(character))[2:]) 
        serial.append(bin(ord(character))[2:]) 

    serial = ' '.join(serial)
    return serial

def main():
    x = "Hello world"

    print(string_to_binary(x))


# Take in image for encoding.
#im = Image.open(io)

# Must pass tuple of x,y cooridnate of pixel you want.
#im.getpixel((0,0))

# Serialise a message into binary.

# Get size of image --  width and height

if __name__ == "__main__":
    main()
