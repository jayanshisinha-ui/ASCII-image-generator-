
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

with open("abhinavbindra.ppm", "r") as file:
    lines = file.readlines()

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

index = 0

with open("generated.txt", "w") as out:
    for y in range(new_height):
        for x in range(new_width):
            
            px = ((y * scale * 2) * width + (x * scale)) * 3
            r = int(pixels[px])
            g = int(pixels[px + 1])
            b = int(pixels[px + 2])

            intensity = (r + g + b) // 3
            out.write(getChar(intensity))
        out.write("\n")

print("ASCII Image Generated")


