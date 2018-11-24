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


# Class to get the text into an image. Both are specified and an end product 
#   is saved.
class makeSteganograph(text, image):
  def __init__(self, textPath, imagePath):
    self.text = text(textPath)
    self.image = image(imagePath)
    self.serialisedText = stringToInt(self.text.raw)
    self.nbPixelsNeeded = len(self.serialisedText)
    self.originalPixels = getPixelValues(self.image.image)

  def length(self):
    chars = len(self.text.raw)
    wrds = len(self.text.words)
    w,h = self.image.image.size
    print("Number of characters: \t\t"        + str(chars)  + "\n"
          "Number of words: \t\t"             + str(wrds)   + "\n"
          "Width of image (in pixels): \t"    + str(w)      + "\n"
          "Height of image (in pixels): \t"   + str(h)      + "\n")


class decodeSteganograph(text, image):
  def __init__(self):
    pass



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
  return pix
  
# Encode the text into the image and return an image object as the end 
#   result.
def encode(self):
  pass

def encodePixel(pixel, char):
  shelf = (pixel[0] << 16) | (pixel[1] << 8) | (pixel[2])
  shelf += ord(char)
  leftMask = 255 << 16
  middleMask = 255 << 8
  rightMask = 255
  

def decodePixel()
  pass

# Take in the image with the encoded text and the original image (no encoded
#   text) and return the encoded message.
def decode(self, encoded, original):
  pass
  
# Main -- runs when the script is executed
def main():
  steg = makeSteganograph(textIO, imageIO)
  steg.length()
  print(steg.nbPixelsNeeded)

  print("Max value in steg is: " + str(max(steg.serialisedText)))
  print("Min value in steg is: " + str(min(steg.serialisedText)))

  encodePixel([1,2,3])


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
