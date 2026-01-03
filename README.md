# ASCII-image-generator— Image → Text Converter (Python)

ASCII Art is a visual technique that transforms images into patterns of text characters, recreating photos using symbols instead of pixels. It is a fascinating combination of graphics, mathematics, and creativity — originally used on early computers before image displays existed.

This project allows you to convert any image into ASCII manually using Python. The result can be printed on the terminal or saved as a text/PNG output.

Overview

ASCII Art Maker is a Python-based tool that transforms digital images into text-based artwork. Instead of using pixels, the program rebuilds the image using ASCII characters such as @, %, #, *, and . — each chosen based on how dark or light the original pixel is. This project demonstrates how images can be represented through mathematical processing and character mapping, giving a retro terminal-style visual effect. It is useful for learning image processing fundamentals, working with Python’s Pillow library, and exploring how computers can convert visual data into alternate formats like text.

Objective 

The main objective of this project is to apply programming and digital graphics concepts to develop software that converts images into ASCII artwork. By using Python and mathematical transformations, the project aims to educate users about grayscale processing, data mapping, and how visual content can be expressed in a non-graphical format.

Concept Used 

1. Digital Image Processing
Understanding how images are made of pixels (tiny color blocks)
Accessing and manipulating pixel data using Python

2. RGB to Grayscale Conversion
A mathematical formula is applied to convert colored pixels to grayscale:
Gray = (R + G + B) / 3
This simplifies color information into brightness values (0–255)

3. Character Mapping / Value Mapping

Brightness values are mapped to characters based on density
Darker pixels → symbols like @ or %
Lighter pixels → characters like . or :
This mapping reconstructs the visual shape using text

4. Resizing and Aspect Ratio Adjustment
The image is resized so ASCII characters do not stretch or distort
Text characters are taller than they are wide, so scaling must account for font proportions

5. File Handling in Python
Reading image files
Generating text output files

6.Loops and Iterative Processing
Nested loops are used to scan the image pixel-by-pixel
Each pixel is evaluated and converted into a character

Conclusion

This ASCII Art Converter shows how computing is not limited to numbers and calculations — it can also be creative and artistic. By converting images into characters, the project bridges logic and imagination, giving users a new perspective on how technology can represent visual information.

