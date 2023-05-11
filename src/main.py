
from manim import *
# from manim_slides import Slide


class BasicExample(Scene):
    def construct(self):
        # SLIDE 1

        grid = NumberPlane(
            x_range=(0, 10, 1),
            y_range=(0, 10, 1),
            x_length=5,
            y_length=5,
        )
        grid.flip(LEFT)
        self.add(grid)
        self.play(Create(grid, run_time=3, lag_ratio=0.1))
        self.wait()
        # self.next_slide()  # Waits user to press continue to go to the next slide
