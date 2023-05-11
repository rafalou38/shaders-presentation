from manim import *
from manim_editor import PresentationSectionType

# from manim_slides import Slide
config.disable_caching = True


class Intro(Scene):
    def construct(self):
        # SLIDE 1

        title = Text("Comment fonctione un Ordinateur ?")
        self.add(title)
        self.wait()


class Differences(Scene):
    def construct(self):

        title = Text("Composants").move_to(UP * 3)
        self.add(title)

        cpu_img = ImageMobject("images/01/cpu.png")
        cpu_img.height = 4
        cpu_text = Text("CPU").scale(1).next_to(cpu_img, DOWN)
        cpu_sub_text = (
            Text("(Central Processing Unit)").scale(
                0.5).next_to(cpu_text, DOWN)
        )
        cpu_group = Group(cpu_img, cpu_text, cpu_sub_text)

        self.play(FadeIn(cpu_group))

        self.play(cpu_group.animate.scale(0.75).move_to(RIGHT * -4.5 + UP * 0))

        gpu_img = ImageMobject("images/01/gpu.png")
        gpu_img.height = 4
        gpu_text = Text("GPU").scale(1).next_to(gpu_img, DOWN)
        gpu_sub_text = (
            Text("(Graphics Processing Unit)").scale(
                0.5).next_to(gpu_text, DOWN)
        )
        gpu_group = Group(gpu_img, gpu_text, gpu_sub_text)

        self.play(FadeIn(gpu_group))
        self.play(gpu_group.animate.scale(0.75).move_to(RIGHT * 4.5 + UP * 0))

        arrow_cpu_gpu = DoubleArrow(cpu_img, gpu_img).move_to(UP * -0.5)
        self.play(GrowArrow(arrow_cpu_gpu))

        self.wait()

        self.remove(arrow_cpu_gpu)
        self.play(
            cpu_group.animate.scale(0.5).move_to(RIGHT * -5 + UP * 2),
            gpu_group.animate.scale(0.5).move_to(RIGHT * 5 + UP * 2),
        )

        arch_image = ImageMobject("images/01/cpu-gpu.png")
        arch_image.width = 7
        self.play(FadeIn(arch_image))

        cpu_info = (
            Text(
                """Fréquence: 3.5 GHz - 4.0 GHz
- 4-8 Coeurs
- Latence faible
- Traitement en série
"""
            )
            .scale(0.40)
            .next_to(cpu_group, DOWN)
        )
        gpu_info = (
            Text(
                """Fréquence: 1.0 GHz
- 10000 Coeurs
- I/O élevé
- Traitement en parallel"""
            )
            .scale(0.40)
            .next_to(gpu_group, DOWN)
        )

        self.play(AddTextWordByWord(cpu_info), AddTextWordByWord(gpu_info))
        self.wait()


class CodeCPU(Scene):
    def construct(self):
        self.next_section("B-code.title")
        title = Text("Processeur").move_to(UP * 3.5 + LEFT * 5)
        self.play(Create(title))

        self.next_section("B-code.simple-code")

        code = """
n = 1
for i in range(100):
    if n>0:
        n = n * -11 
    else:
        n = n + 105
    
    print(n)
    """.strip()
        rendered_code = Code(
            code=code,
            tab_width=4,
            background="window",
            language="Python",
            font="Monospace",
            style="fruity",
            line_spacing=0.5,
        )
        rendered_code.width = 6
        rendered_code.move_to(LEFT * 3.5)

        ax = Axes(
            x_range=[0, 100, 3],
            y_range=[-2000, 200, 100],
            axis_config={"include_numbers": False, "color": GRAY},

            tips=False,
        )
        ax.width = 6
        ax.move_to(RIGHT * 3.5)
        xlst = range(100)
        ylst = []
        n = 1
        for i in xlst:
            if n > 0:
                n = n * -11
            else:
                n = n + 105

            ylst.append(n)

        graph = ax.plot_line_graph(xlst, ylst, line_color=color.rgba_to_color(
            (0, 0, 0, 0)), vertex_dot_radius=0.03, vertex_dot_style={"stroke_width": 2, "fill_color": BLUE})

        self.play(Create(ax), AddTextWordByWord(rendered_code))  # type: ignore

        self.next_section("B-code.simple-graph")
        self.play(Create(graph), run_time=5)

        self.next_section("B-code.michel-base")

        self.play(FadeOut(ax), FadeOut(graph), FadeOut(rendered_code))

        with open("scripts/michel.py", "r") as f:
            code = f.read()

        michelCode = Code(
            code=code,
            tab_width=4,
            background="window",
            language="Python",
            font="Monospace",
            style="fruity",
            line_spacing=0.5,
        ).scale_to_fit_height(6)

        michelBase = ImageMobject(
            "images/michel.jpg")
        michelBase.height = 4
        # michelCode.to_corner()
        self.play(GrowFromCenter(michelBase))

        self.next_section("B-code.michel-code")

        self.play(michelBase.animate.scale(0.75).move_to(RIGHT * 5 + UP * 2))

        self.play(GrowFromCenter(michelCode))
        self.next_section("B-code.michel-result")
        # self.play(michelCode.animate.to_corner(LEFT + DOWN))

        michelAfter = ImageMobject(
            "images/michel-b.png").move_to(RIGHT * 5 + DOWN * 2)
        michelAfter.height = 4

        michelAfter.scale(0.75)

        arrow = Arrow(michelBase.get_bottom(), michelAfter.get_top())

        self.play(GrowFromCenter(michelAfter), GrowArrow(arrow))

        metrics = Text("""
        Dimensions de l'image: 1200x1600
        => 1_920_000 pixels 
        ~ 30 op / pixel
        30_920_000 op pour 1 image

        CPU 3Ghz = 3_000_000_000 op / s
        """)
