from PIL import Image
img_base = Image.open('images/Big_Buck_Bunny_4K.webm.720p.jpg')
pixels_base = img_base.load()
width = img_base.size[0]
height = img_base.size[1]

img_new = Image.new( img_base.mode, img_base.size)
pixels_new = img_new.load()


for x in range(width):
    for y in range(height):
        if pixels_base[x,y][0]>150:
            pixels_new[x,y] = (
                255,
                int(pixels_base[x,y][1]/2),
                int(pixels_base[x,y][2]/2),
            )
        else:
            pixels_new[x,y] = pixels_base[x,y]


img_new.save("out.png")