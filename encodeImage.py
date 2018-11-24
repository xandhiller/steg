from PIL import Image

imageIO = 'jim.jpg'
textIO = 'othello.txt'

class text:
  def __init__(self, path):
    f = open(path, 'r')
    self.text = f.read()
    self.words = self.text.split(' ') # Split the words over spaces.
        
class image:
  def __init__(self, path):
    self.image = Image.open(path)
    self.width = self.image.width 
    self.height = self.image.height

# String to binary array
def stringToBinary(string):
  serial = []
  for character in string:
    serial.append(int(bin(ord(character))[2:]))
  return serial

def main():

  txt = text(textIO)
  img = image(imageIO)
  
  print(len(txt.text))

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
