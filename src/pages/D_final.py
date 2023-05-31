from PIL import Image
from manim import *
from manim_slides import Slide

# MandelBroot


class F1(Slide):
    def construct(self):
        title = Text("Autres usages").scale(2)
        self.play(Write(title))
        self.wait(0.5)
        self.next_slide()
        self.wait(0.5)


class F2(Slide):
    def construct(self):
        title = Text("Fin").scale(4)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.become(
            Text("Sources").scale(0.75).to_edge(UP)))

        sources = Text("""
- https://www.shadertoy.com
- Schema architecture:  scan.co.uk
- Big_Buck_Bunny: https://fr.wikipedia.org/wiki/Big_Buck_Bunny
- Julia: http://www.juliasets.dk/Julia.htm
- SmoothLife: chronos
- Fractal Land: Kali
- Fractal Cave: Inigo Quilez, @iquilezles and iquilezles.org
                       """.strip()).scale(0.5)

        self.play(Write(sources))
        self.wait()
        self.next_slide()
