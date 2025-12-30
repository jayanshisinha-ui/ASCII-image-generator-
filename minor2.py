from PIL import Image,ImageDraw
import math

characters = "@%#*+=-:."

charArray = list(characters)
Length = len(charArray)
val = Length/256

SFactor = 0.09
Width = 8
Height = 18

def getChar(inputInt):
    return charArray[math.floor(inputInt* val)]
    
text_file =open("generated.txt","w")
image = Image.open("abhinavbindra.png")


width, height = image.size
print(width,height,height/width)
image = image.resize((int(SFactor*width), int(SFactor*height*(Width/Height))),Image.NEAREST)
width, height = image.size
pix = image.load()

GeneratedImage = Image.new('RGB',(Width*width , Height*height),color = (0,0,0))

for i in range(height):
    for j in range(width):
        r,g,b = pix[j,i]
        print(r) 
        h = int(r/3 + g/3 + b/3)
        pix[j,i]=(h,h,h)
        text_file.write(getChar(h))

    text_file.write('\n')    

GeneratedImage.save('generated.txt')


