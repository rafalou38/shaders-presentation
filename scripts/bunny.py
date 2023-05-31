from PIL import Image
from math import sqrt, pow
img_base = Image.open('images/bunny.jpg')
pixels_base = img_base.load()
width = img_base.size[0]
height = img_base.size[1]

img_new = Image.new(img_base.mode, img_base.size)
pixels_new = img_new.load()


target_color = (147, 202, 255)

for x in range(width):
    for y in range(height):
        pixel = pixels_base[x, y]
        if (sqrt(
            pow(pixel[0] - target_color[0], 2) +
            pow(pixel[1] - target_color[1], 2) +
            pow(pixel[2] - target_color[2], 2)
        ) < 70):
            pixels_new[x, y] = (
                int(pixel[0]),
                int(pixel[1]/5),
                int(pixel[2]),
            )
        else:
            pixels_new[x, y] = pixels_base[x, y]

img_new.save("out.png")
