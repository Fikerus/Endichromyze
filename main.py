import os
import sys
from datetime import datetime
from PIL import Image

clear = lambda: os.system("cls")
clear()

folder = input("Название папки внутри этой папки: \n")
# folder = "папка"
clear()

path = f"{os.getcwd()}\\{folder}"

# print(folder)
# print(path)

color1 = input("Введите RGB цвет (через пробел) который не нужно заменять: \n")
# color1r = int(input("R: "))
# color1g = int(input("G: "))
# color1b = int(input("B: "))
color1r, color1g, color1b = map(lambda x: int(x),color1.split(" "))

color2 = input("\nВведите RGB цвет на который нужно заменить всё, кроме предыдущего цвета: \n")
# color2r = int(input("R: "))
# color2g = int(input("G: "))
# color2b = int(input("B: "))
color2r, color2g, color2b = map(lambda x: int(x),color2.split(" "))

clear()

f = []
for (dirpath, dirnames, filenames) in os.walk(path):
    f.extend(filenames)
    break

if input(f"\nВаши цвета:\nПервый цвет: {color1r} {color1g} {color1b}\nВторой цвет: {color2r} {color2g} {color2b}\nВаши файлы: {f}\nПродолжить? [Enter]\n") != "": quit()

timenow = datetime.now().strftime("%H_%M_%S")

os.system(f"mkdir {folder}_{timenow}")

for item in f:
    # Import an image from directory:
    input_image = Image.open(f"{path}\\{item}")
    
    # Extracting pixel map:
    pixel_map = input_image.load()
    
    # Extracting the width and height 
    # of the image:
    width, height = input_image.size

    for x in range(width):
        for y in range(height):
            r, g, b = input_image.getpixel((x, y))
            # print(r,g,b)
            if not(r==color1r and g==color1g and b==color1b):
                pixel_map[x,y] = (color2r, color2g, color2b)
    input_image.save(f"{folder}_{timenow}\\{item}")