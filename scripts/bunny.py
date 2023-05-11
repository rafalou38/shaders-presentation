from PIL import Image
from math import sqrt
img_base = Image.open('images/obi-wan-grievous-hi-there_1.jpg')
pixels_base = img_base.load()
width = img_base.size[0]
height = img_base.size[1]

img_new = Image.new( img_base.mode, img_base.size)
pixels_new = img_new.load()


for x in range(width):
    for y in range(height):
        pixels_new[x,y] = (
            int(pow(pixels_base[x,y][1], 2) / 100) ,
            int(pow(pixels_base[x,y][2], 2) / 100) ,
            int(pow(pixels_base[x,y][1], 2) / 100) ,
        )

img_new.save("out.png")