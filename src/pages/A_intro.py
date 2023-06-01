from manim import *
from manim_slides import Slide
# from manim_slides import Slide
# config.disable_caching = True


# Differences
class INTRO(Slide):
    def construct(self):
        title = Text("Les Shaders").scale(2)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)
        self.next_slide()

        self.play(title.animate.scale_to_fit_height(
            0.5).to_edge(UP), run_time=0.8)

        plan = Text("""
1. Architecture d'un ordinateur
2. Maths et shaders
3. Exemples de shaders
""", fill_opacity=0.8)
      #   plan.scale(3)
        self.play(Write(plan), run_time=0.8)
        self.wait(0.5)
        self.next_slide()
        self.wait(0.5)
