from PIL import Image
from manim import *
from manim_slides import Slide
import math


class M1(Slide):
    def construct(self):
        title = Text("Le shader")

        self.play(Write(title))
        self.wait(0.5)
        self.next_slide()
        self.play(FadeOut(title))

        # GRID
        squares = []
        for y in range(20):
            for x in range(25):
                w = 6 / 20
                sq = Square(w, stroke_width=1, stroke_color=GRAY).shift(
                    LEFT * x * w + DOWN * y * w)

                squares.append(sq)

        sqGroup = Group(*squares).move_to(LEFT * 0)
        self.play(FadeIn(sqGroup))

        # END GRID

        self.wait(0.5)
        self.next_slide()

        # => BASE FUNCTION

        baseFn = MathTex(r"Shader: (x,y)\mapsto (r,g,b,a)",
                         font_size=60).next_to(sqGroup, UP)
        self.play(Write(baseFn), run_time=0.5)

        self.wait(0.5)
        self.next_slide()

        # => FULL FUNCTION

        fullFn = MathTex(r"Shader: (x,y)\mapsto (1,0,0,1)",
                         font_size=60).next_to(sqGroup, UP)
        self.play(Transform(baseFn, fullFn))

        anims = []
        for x in range(25):
            for y in range(20):
                w = 6 / 20

                # if ((x - 25/2) ** 2 + (y - 10) ** 2 < 8**2):
                sq = squares[y * 25 + x]

                anims.append(sq.animate.set_fill(RED, 1))

        self.play(Succession(*anims), run_time=1)
        self.wait(1)

        self.next_slide()

        # => Circle

        anims = []
        for x in range(25):
            for y in range(20):
                w = 6 / 20

                sq = squares[y * 25 + x]
                if ((x - 25/2) ** 2 + (y - 10) ** 2 < 8**2):
                    anims.append(sq.animate.set_fill(RED, 1))
                else:
                    anims.append(sq.animate.set_fill(RED, 0))

        self.play(Succession(*anims), run_time=1)
        self.wait(1)

        self.next_slide()

        cirlcFn = MathTex(r"(x,y)\mapsto (x - 10)^2 + (y - 10)^2 < 8^2",
                          font_size=60).next_to(sqGroup, UP)
        self.play(Transform(baseFn, cirlcFn))

        self.wait(0.5)
        self.next_slide()
        self.wait(0.5)


# Sens des équations
class M2(Slide):
    def construct(self):
        subtitle = Text("Le Cercle")

        self.play(Write(subtitle), run_time=0.5)
        self.wait(0.5)
        self.next_slide()
        self.clear()

        self.circle()
        self.clear()
        self.line()

        self.wait(0.5)
        self.next_slide()
        self.wait(0.5)
        self.next_slide()

    def line(self):
        subtitle = Text("Droite")

        self.play(Write(subtitle), run_time=0.5)
        self.wait(0.5)
        self.next_slide()
        self.clear()

        # Create axes
        axes = Axes(
            x_range=(0, 1),
            y_range=(0, 1),
            x_length=6,
            y_length=6,
            axis_config={
                "include_tip": False,
                "include_numbers": True,
                "stroke_width": 2,

            }
        )
        axes.to_edge(RIGHT)

        a_track = ValueTracker(0)
        b_track = ValueTracker(-1)
        c_track = ValueTracker(0.5)  # type: ignore

        parametersDisplay = Text(f"a = {round(a_track.get_value(), 2)} \nb = {round(b_track.get_value(), 2)} \nc = {round(c_track.get_value(), 2)}",
                                 font_size=50)
        parametersDisplay.to_edge(LEFT)

        eq = MathTex(r"ax + by + c = 0",
                     font_size=80).next_to(parametersDisplay, UP, aligned_edge=LEFT)

        def fn(x):
            if (b_track.get_value() == 0):
                return 100
            return min(100, max(-100, (-a_track.get_value() * x - c_track.get_value())/b_track.get_value()))

        line = axes.plot(fn, [0, 1], use_smoothing=False)

        def updater(e):
            e.clear_points()
            e.generate_points()

        self.play(Write(eq), Create(axes))

        self.wait(0.5)
        self.next_slide()

        self.play(Write(parametersDisplay), Create(line))

        line.add_updater(updater)

        def updateEq(e):
            eq_n = Text(f"a = {round(a_track.get_value(), 2)} \nb = {round(b_track.get_value(), 2)} \nc = {round(c_track.get_value(), 2)}",
                        font_size=50).to_edge(LEFT)
            e.become(eq_n)
        parametersDisplay.add_updater(updateEq)
        self.wait(0.5)
        self.next_slide()

        self.play(a_track.animate.set_value(-1))

        self.wait(0.5)
        self.next_slide()

        self.play(b_track.animate.set_value(1))

        self.wait(0.5)
        self.next_slide()

        self.play(c_track.animate.set_value(-0.5))

        self.wait(0.5)
        self.next_slide()

        #
        # Circle
        #

    def circle(self):
        eq = MathTex(r"l = \sqrt{x^2 + y^2}",
                     font_size=75).to_corner(UP + LEFT)
        plane = NumberPlane()
        vector_1 = Vector([1, 2])
        l1 = math.sqrt(1*1 + 2*2)
        t1 = Text(str(round(l1 * 10) / 10)).move_to([1.2, 2.2, 0]).scale(0.5)
        vector_2 = Vector([3, 2])
        l2 = math.sqrt(3*3 + 2*2)
        t2 = Text(str(round(l2 * 10) / 10)).move_to([3.2, 2.2, 0]).scale(0.5)
        self.play(Create(plane), Create(vector_1), Create(vector_2))
        self.play(Write(eq), Create(t1), Create(t2))
        self.wait(0.5)
        self.next_slide()

        circ_1 = Circle(l1)
        # circ_2 = Circle(l2)
        eq2 = MathTex(r"x^2 + y^2 = r^2",
                      font_size=75).to_corner(DOWN + LEFT)

        self.play(Write(eq2), Create(circ_1))
        self.wait(0.5)
        self.next_slide()

        circ_2 = Circle(1).move_to(RIGHT * 4 + DOWN)
        eq3 = MathTex(r"(x-a)^2 + (y-b)^2 = r^2",
                      font_size=75).to_corner(DOWN + LEFT)
        self.play(Create(circ_2))
        self.wait(0.5)
        self.next_slide()
        self.play(eq2.animate.become(eq3))
        self.wait(0.5)
        self.next_slide()
