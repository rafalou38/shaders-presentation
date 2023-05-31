from manim import *
from manim_slides import Slide
# from manim_slides import Slide
# config.disable_caching = True

# Differences


class PC1(Slide):
    def construct(self):
        title = Text("L'architecture d'un ordinateur")
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)
        self.next_slide()
        self.remove(title)

        cpu_img = ImageMobject("images/01/cpu.png")
        cpu_img.height = 4
        cpu_text = Text("CPU").scale(1).next_to(cpu_img, DOWN)
        cpu_sub_text = (
            Text("(Central Processing Unit)").scale(
                0.5).next_to(cpu_text, DOWN)
        )
        cpu_group = Group(cpu_img, cpu_text, cpu_sub_text)

        self.play(FadeIn(cpu_group))
        self.next_slide()

        self.play(cpu_group.animate.scale(0.8).move_to(
            RIGHT * -4.5 + UP * 0), run_time=0.8)

        gpu_img = ImageMobject("images/01/gpu.png")
        gpu_img.height = 4
        gpu_text = Text("GPU").scale(1).next_to(gpu_img, DOWN)
        gpu_sub_text = (
            Text("(Graphics Processing Unit)").scale(
                0.5).next_to(gpu_text, DOWN)
        )
        gpu_group = Group(gpu_img, gpu_text, gpu_sub_text)

        self.play(FadeIn(gpu_group))
        self.next_slide()
        self.play(gpu_group.animate.scale(0.8).move_to(RIGHT * 4.5 + UP * 0))

        arrow_cpu_gpu = DoubleArrow(cpu_img, gpu_img).move_to(UP * -0.5)
        self.play(GrowArrow(arrow_cpu_gpu), run_time=0.8)

        self.wait(0.5)
        self.next_slide()

        self.remove(arrow_cpu_gpu)
        self.play(
            cpu_group.animate.scale(0.8).move_to(RIGHT * -5 + UP * 2),
            gpu_group.animate.scale(0.8).move_to(RIGHT * 5 + UP * 2), run_time=0.8
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
            .scale(0.35)
            .next_to(cpu_group, DOWN).shift(DOWN * 2)
        )
        gpu_info = (
            Text(
                """Fréquence: 1.0 GHz
- 10000 Coeurs
- I/O élevé
- Traitement en parallel"""
            )
            .scale(0.35)
            .next_to(gpu_group, DOWN).shift(DOWN * 2)
        )

        self.play(Write(cpu_info), Write(gpu_info), run_time=0.8)
        self.wait(0.5)
        self.next_slide()
        self.wait(0.5)


class PC2(Slide):
    def construct(self):
        title = Text("Exemple de code pour processeur").scale(0.8).to_edge(UP)
        self.play(Write(title), run_time=0.5)
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

        self.play(Create(ax), Write(rendered_code))  # type: ignore

        self.wait(0.5)
        self.next_slide()
        self.play(Create(graph), run_time=3)

        self.wait(0.5)
        self.next_slide()

        self.play(FadeOut(ax), FadeOut(graph), FadeOut(rendered_code))

        with open("scripts/bunny.py", "r") as f:
            code = f.read()

        michelCode = Code(
            code=code,
            tab_width=4,
            background="window",
            language="Python",
            font="Monospace",
            style="fruity",
            line_spacing=0.5,
        ).scale_to_fit_height(6).to_edge(DOWN)

        michelBase = ImageMobject(
            "images/bunny.jpg")
        michelBase.width = 10
        # michelCode.to_corner()
        self.play(title.animate.become(
            Text("Traitement d'image").scale(0.8).to_edge(UP)), GrowFromCenter(michelBase))

        self.wait(0.5)
        self.next_slide()

        self.play(michelBase.animate.scale_to_fit_width(
            3.5).move_to(RIGHT * 5 + UP * 2))

        self.play(GrowFromCenter(michelCode))
        self.wait(0.5)
        self.next_slide()
        # self.play(michelCode.animate.to_corner(LEFT + DOWN))

        michelAfter = ImageMobject(
            "images/bunny-after.png").move_to(RIGHT * 5 + DOWN * 2)
        michelAfter.height = 4

        michelAfter.scale_to_fit_width(3.5)

        arrow = Arrow(michelBase.get_bottom(), michelAfter.get_top())

        self.play(GrowFromCenter(michelAfter), GrowArrow(arrow))

        self.wait(0.5)
        self.next_slide()

        metrics = Text("""
        ~ 4000 op / pixel

        Notre image:
        1280 × 720
        => 921_600 pixels
        => 3_686_400_000 op 
        """).scale(0.40).to_edge(LEFT).shift(UP * 2)

        metrics4k = Text("""
        Image 4k: 
        4096 × 2160
        => 8_847_360 pixels 
        => 35_389_440_000 op
        """).scale(0.40).to_edge(LEFT).shift(DOWN * 2)

        self.play(Create(metrics))
        self.wait(0.5)
        self.next_slide()

        self.play(Create(metrics4k))
        self.wait(0.5)
        self.next_slide()
        self.wait(0.5)
