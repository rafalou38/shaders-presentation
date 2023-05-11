from PIL import Image
from math import sqrt

img_base = Image.open("images/michel.jpg")
pixels_base = img_base.load()
width = img_base.size[0]
height = img_base.size[1]

img_new = Image.new(img_base.mode, img_base.size)
pixels_new = img_new.load()


for x in range(width):
    for y in range(height):
        if (
            pixels_base[x, y][0] > 100
            and pixels_base[x, y][1] > 100
            and pixels_base[x, y][1] > 100
        ):
            pixels_new[x, y] = (
                int(pixels_base[x, y][0] - 100),
                int(pixels_base[x, y][1] - 100),
                int(pixels_base[x, y][2] - 100),
            )
        else:
            pixels_new[x, y] = (
                int(pixels_base[x, y][0]),
                int(pixels_base[x, y][1]),
                int(pixels_base[x, y][2]),
            )

img_new.save("images/michel-b.png")
