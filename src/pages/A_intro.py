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
   1. Difference HARDWARE entre CPU et GPU
   2. Pourquoi est ce qu'on a besoin du GPU
2. Maths et shaders
   1. Modèle mathématique
   2. Fonctionnement précis
3. Exemples de shaders
   1. Cercle
   2. Ensemble de Julia
   3. Smooth life
   4. En 3D
   5. Le Ray Tracing
""")
        plan.scale_to_fit_height(6.5).next_to(title, DOWN)
        self.play(Write(plan), run_time=0.8)
        self.wait(0.5)
        self.next_slide()
        self.wait(0.5)
