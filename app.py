import gradio as gr
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

def generate_ascii(image):
    if image is None:
        return "<pre>Please upload an image!</pre>"

    image = image.convert("RGB")
    width, height = image.size

    image = image.resize((int(SFactor * width), int(SFactor * height * (Width / Height))), Image.NEAREST)
    width, height = image.size
    pix = image.load()

    output_text = ""

    for i in range(height):
        for j in range(width):
            r, g, b = pix[j, i]
            intensity = int(r/3 + g/3 + b/3)
            output_text += getChar(intensity)
        output_text += "\n"

    # Wrap inside HTML <pre> tag to show exact shape
    return f"<pre style='font-size:10px;line-height:10px;font-family:monospace;'>{output_text}</pre>"

with gr.Blocks() as demo:
    gr.Markdown("## 🧠 Image → ASCII Art Generator (Better UI Version)")

    img_input = gr.Image(type="pil", label="Upload Image")
    btn = gr.Button("Generate ASCII")

    output_html = gr.HTML()

    btn.click(generate_ascii, inputs=img_input, outputs=output_html)

demo.launch()
