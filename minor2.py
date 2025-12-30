from PIL import Image
import math

character = "@%#*+=-:."
charArray = list(character)
Length = len(charArray)
val = Length / 256

SFactor = 0.09
Width = 8
Height = 18

def getChar(inputInt):
    return charArray[math.floor(inputInt * val)]

image = Image.open("abhinavbindra.png")

width, height = image.size
image = image.resize((int(SFactor * width), int(SFactor * height * (Width / Height))), Image.NEAREST)
width, height = image.size
pix = image.load()

text_file = open("generated.txt", "w")

for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        intensity = int((r + g + b) / 3)
        text_file.write(getChar(intensity))
    text_file.write("\n")

text_file.close()
print("ASCII Image Generated Successfully!")

