
import gradio as gr

characters = "@%#*+=-:."
charArray = list(characters)
length = len(charArray)

def getChar(intensity):
    intensity = int((intensity - 40) * 255 / (220 - 40))
    if intensity < 0:
        intensity = 0
    if intensity > 255:
        intensity = 255
    index = int(intensity * (length - 1) / 255)
    return charArray[index]

def ppm_to_ascii(ppm_file):
    lines = ppm_file.decode("utf-8").splitlines()

    data = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            data.extend(line.split())

    width = int(data[1])
    height = int(data[2])
    pixels = data[4:]

    scale = 8
    new_width = width // scale
    new_height = height // (scale * 2)

    ascii_art = []
    for y in range(new_height):
        row = ""
        for x in range(new_width):
            px = ((y * scale * 2) * width + (x * scale)) * 3
            r = int(pixels[px])
            g = int(pixels[px + 1])
            b = int(pixels[px + 2])
            intensity = (r + g + b) // 3
            row += getChar(intensity)
        ascii_art.append(row)

    return "\n".join(ascii_art)

demo = gr.Interface(
    fn=ppm_to_ascii,
    inputs=gr.File(label="Upload P3 PPM File"),
    outputs=gr.Textbox(lines=25, label="ASCII Output"),
    title="PPM to ASCII Art Converter",
    description="Upload a P3 .ppm image and convert it into ASCII art."
)

if __name__ == "__main__":
    demo.launch()
