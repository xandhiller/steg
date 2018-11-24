from PIL import Image

imageIO = 'jim.jpg'
textIO = 'othello.txt'

################################################################################
# Classes
################################################################################

class text:
  def __init__(self, path):
    f = open(path, 'r')
    self.raw = f.read()
    self.words = self.raw.split(' ') # Split the words over spaces.

        
class image:
  def __init__(self, path):
    self.image = Image.open(path)
    self.width = self.image.width 
    self.height = self.image.height


class steganograph(text, image):
  def __init__(self, textPath, imagePath):
    self.text = text(textPath)
    self.image = image(imagePath)
    self.serialisedText = stringToInt(self.text.raw)

  def length(self):
    chars = len(self.text.raw)
    wrds = len(self.text.words)
    w,h = self.image.image.size
    print("Number of characters: \t\t"        + str(chars)  + "\n"
          "Number of words: \t\t"             + str(wrds)   + "\n"
          "Width of image (in pixels): \t"    + str(w)      + "\n"
          "Height of image (in pixels): \t"   + str(h)      + "\n")





################################################################################
# Functions
################################################################################

# String to integer array
# Integers are the unicode value of that integer in unicode.
def stringToInt(string):
  serial = []
  for character in string:
    serial.append(int(ord(character)))
  return serial

# Assumes img is an 'Image' object from PIL
def getPixelValues(img):
  pix = []
  for i in range(img.height):
    for j in range(img.width):
      loc = (j,i) #NOTE: Location has to be a tuple
      p = img.getpixel(loc)
      p = list(p) # Format data to be able to be edited.
      pix.append(p)
  
  
# Main -- runs when the script is executed
def main():
  steg = steganograph(textIO, imageIO)
  steg.length()
  print(steg.serialisedText)




################################################################################
# Admin
################################################################################
if __name__ == "__main__":
    main()

################################################################################ 
# Notes
################################################################################ 

#TODO:
# Serialise a message into binary.
# Get size of image --  width and height
# When doing arithmetic adding letters in, have to handle for overflow issues,
#   recall that the text has to be recoverable, so you must be able to pull it 
#   out with an inverse method.


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
