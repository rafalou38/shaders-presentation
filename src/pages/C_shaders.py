from PIL import Image
from manim import *
from manim_slides import Slide
import cv2
import numpy as np


def process(code, sz=1000):
    # Define the dimensions of the image
    height = sz
    width = sz

    # Create an empty RGBA image data array
    image_data = np.zeros((height, width, 4), dtype=np.uint8)

    # Execute the code string to get the mainImage function
    namespace = {}
    exec(code, namespace)
    mainImage = namespace['mainImage']

    # Evaluate the color of each pixel using the mainImage function
    for i in range(height):
        for j in range(width):
            x = j / width
            y = i / height
            color = [n*255 for n in mainImage(x, y)]
            image_data[i, j] = color

    return image_data


# Cercle
class S1(Slide):
    def construct(self):
        title = Text("Shader - Cercle").scale(0.5).to_edge(UP)
        self.play(Write(title))

        cirlcFn = MathTex(r"(x - C_x)^2 + (y - C_y)^2", r" = ", r"r^2",
                          font_size=90)

        self.play(Write(cirlcFn))
        self.next_slide()
        cirlcFnBis = MathTex(r"(x - C_x)^2 + (y - C_y)^2", r"- r^2", r" = ", r"0",
                             font_size=90)

        self.play(TransformMatchingTex(cirlcFn, cirlcFnBis))

        self.next_slide()

        self.play(FadeOut(cirlcFnBis))
        codes = [
            """
def mainImage(x, y):
    radius = 0.25;
    dist = (x - 0.5) ** 2 + (y - 0.5) ** 2 - radius ** 2
    
    if(dist == 0):
        return (1,1,1,1)
    else:
        return (0,0,0,1)
""".strip(),
            """
def mainImage(x, y):
    radius = 0.25;
    dist = (x - 0.5) ** 2 + (y - 0.5) ** 2 - radius ** 2
    
    if(round(dist*100)/100 == 0):
        return (1,1,1,1)
    else:
        return (0,0,0,1)
""".strip(),
            """
def mainImage(x, y):
    radius = 0.25;
    dist = (x - 0.5) ** 2 + (y - 0.5) ** 2
    
    if(dist < radius ** 2):
        return (1,1,1,1)
    else:
        return (0,0,0,1)
""".strip(),
            """
def mainImage(x, y):
    radius = 0.25;
    dist = (x - 0.5) ** 2 + (y - 0.5) ** 2
    
    if(dist > radius ** 2):
        return (1,1,1,1)
    else:
        return (0,0,0,1)
""".strip(),
            """
def mainImage(x, y):
    dist = (x - 0.5) ** 2 + (y - 0.5) ** 2
    radius = 0.25;
    
    if(dist < radius ** 2):
        return (dist*10,dist*10, dist*10,1)
    else:
        return (0,0,0,1)
""".strip(),
        ]

        prevCode = None
        prevImg = None
        for code in codes:
            codeObj = Code(
                code=code,
                tab_width=4,
                background="window",
                language="Python",
                font="Monospace",
                style="fruity",
                line_spacing=0.5,
            ).scale_to_fit_width(10)

            img = process(code)
            img_mobject = ImageMobject(img).to_edge(RIGHT)
            img_mobject.height = 6

            if (prevCode == None and prevImg == None):
                self.play(Write(codeObj))
                self.next_slide()
                self.play(codeObj.animate.scale_to_fit_width(
                    6).to_edge(LEFT), GrowFromCenter(img_mobject))
                prevCode = codeObj
            else:
                codeObj.scale_to_fit_width(6).to_edge(LEFT)
                self.play(FadeOut(prevImg), FadeIn(img_mobject),
                          Transform(prevCode, codeObj))

            prevImg = img_mobject

            self.next_slide()
        self.wait(0.5)


# MandelBroot
class S2(Slide):
    def construct(self):
        title = Text("Exemples sophistiquées")
        self.play(Write(title))
        self.next_slide()

        self.play(title.animate.become(
            Text("Ensemble de Julia").scale(0.5).to_edge(UP)))
        eq = MathTex(r"{\displaystyle z_{n+1}=z_{n}^{2}+c.}", font_size=96)
        self.play(Write(eq))
        self.next_slide()

        julia = ImageMobject(
            "images/julia07.jpg").scale_to_fit_height(config.frame_height)
        self.play(FadeIn(julia))
        self.next_slide()

        self.clear()
        t = Text("LIFE")
        self.play(Create(t))
        self.next_slide()

        self.clear()
        t = Text("WORLD")
        self.play(Create(t))
        self.next_slide()
        self.clear()

        cave = ImageMobject(
            "images/cave.png").scale_to_fit_height(config.frame_height)
        self.play(FadeIn(cave))
        self.wait(0.5)
        self.next_slide()
        self.wait(0.5)
