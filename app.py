import gradio as gr
from PIL import Image
import math

characters = "@%#*+=-:."
charArray = list(characters)
Length = len(charArray)
val = Length / 256

SFactor = 0.09
Width = 8
Height = 18

def getChar(inputInt):
    return charArray[math.floor(inputInt * val)]

def image_to_ascii(image):
    if image is None:
        return "No image selected"

    width, height = image.size
    image = image.resize((int(SFactor * width), int(SFactor * height * (Width / Height))), Image.NEAREST)
    width, height = image.size
    pix = image.load()

    ascii_art = ""
    for i in range(height):
        for j in range(width):
            r, g, b = pix[j, i]
            intensity = int((r + g + b) / 3)
            ascii_art += getChar(intensity)
        ascii_art += "\n"
    return ascii_art

ui = gr.Interface(
    fn=image_to_ascii,
    inputs=gr.Image(type="pil"),
    outputs=gr.Textbox(lines=40),
    title="Image to ASCII Generator",
    description="Upload an image and convert it into ASCII text art."
)

ui.launch()
