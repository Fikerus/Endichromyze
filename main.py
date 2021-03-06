import os
from datetime import datetime
from PIL import Image

def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
clear()

folder = input("Name of the folder within current folder: \n")
clear()

path = os.path.join(os.getcwd(),folder)

color1 = input("The color you wish not to change: \n")
color1r, color1g, color1b = map(lambda x: int(x),color1.split(" "))

color2 = input("\nThe color which everything else will be changed to: \n")
color2r, color2g, color2b = map(lambda x: int(x),color2.split(" "))

clear()

f = []
for (dirpath, dirnames, filenames) in os.walk(path):
    f.extend(filenames)
    break

f = list(filter(lambda x:x[-4:] in (".bmp", ".png"),f))

print(f"Your colors:\nThe first color: {color1r} {color1g} {color1b}\nThe second color: {color2r} {color2g} {color2b}\nYour files: {f}\n")
input(f"Do you wish to continue? [Enter]\n")

timenow = datetime.now().strftime("%H_%M_%S")

os.system(f"mkdir {folder}_{timenow}")

for item in f:
    # Import an image from directory:
    input_image = Image.open(os.path.join(path,item))
    
    # Extracting pixel map:
    pixel_map = input_image.load()
    
    # Extracting the width and height 
    # of the image:
    width, height = input_image.size

    for x in range(width):
        for y in range(height):
            r, g, b = input_image.getpixel((x, y))
            if not(r==color1r and g==color1g and b==color1b):
                pixel_map[x,y] = (color2r, color2g, color2b)
    input_image.save(os.path.join(f"{folder}_{timenow}", item))
