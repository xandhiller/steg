from PIL import Image

imageIo = 'jim.jpg'
# textIo

class text:
  def __init__(self, path):
    pass
        
class image:
  def __init__(self, path):
    pass 

# String to binary array
def stringToBinary(string):
  serial = []
  for character in string:
    serial.append(int(bin(ord(character))[2:]))
  return serial

def main():

if __name__ == "__main__":
    main()

################################################################################ 

#TODO:
# Serialise a message into binary.
# Get size of image --  width and height


#HOWTO:

# Take in image for encoding.
#im = Image.open(io)

# Must pass tuple of x,y cooridnate of pixel you want.
#im.getpixel((0,0))

# How to use stringToBinary(string)
# x = "Hello world"
# print("x before edit: ")
# print(x)
# print(type((x)))
# x = stringToBinary(x)
# print("x after edit: ")
# print(x) 
# print(type(x))
