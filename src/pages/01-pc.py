from manim import *
# from manim_slides import Slide


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
        cpu_img.height=4
        cpu_text = Text("CPU").scale(1).next_to(cpu_img, DOWN)
        cpu_sub_text = Text("(Central Processing Unit)").scale(0.5).next_to(cpu_text, DOWN)
        cpu_group = Group(cpu_img,cpu_text,cpu_sub_text)

        self.play(FadeIn(cpu_group))

        self.play(cpu_group.animate.scale(0.75).move_to(RIGHT * -4.5 + UP * 0))

        gpu_img = ImageMobject("images/01/gpu.png")
        gpu_img.height=4
        gpu_text = Text("GPU").scale(1).next_to(gpu_img, DOWN)
        gpu_sub_text = Text("(Graphics Processing Unit)").scale(0.5).next_to(gpu_text, DOWN)
        gpu_group = Group(gpu_img,gpu_text,gpu_sub_text)

        self.play(FadeIn(gpu_group))
        self.play(gpu_group.animate.scale(0.75).move_to(RIGHT * 4.5 + UP * 0))

        arrow_cpu_gpu = DoubleArrow(cpu_img, gpu_img).move_to(UP * -0.5)
        self.play(Create(arrow_cpu_gpu))

        self.wait()

        self.remove(arrow_cpu_gpu)
        self.play(
            cpu_group.animate.scale(0.5).move_to(RIGHT * -5 + UP * 2),
            gpu_group.animate.scale(0.5).move_to(RIGHT * 5 + UP * 2)
        )

        arch_image = ImageMobject("images/01/cpu-gpu.png")
        arch_image.width = 7
        self.play(FadeIn(arch_image))

        cpu_info = Text(
"""Fréquence: 3.5 GHz - 4.0 GHz
- 4-8 Coeurs
- Latence faible
- Traitement en série
""").scale(0.40).next_to(cpu_group, DOWN)
        gpu_info = Text("""Fréquence: 1.0 GHz
- 10000 Coeurs
- I/O élevé
- Traitement en parallel""").scale(0.40).next_to(gpu_group, DOWN)

        self.play(AddTextWordByWord(cpu_info), AddTextWordByWord(gpu_info))
        self.wait()


class CodeCPU(Scene):
    def construct(self):
        title = Text("Processeur").move_to(UP * 3)
        self.add(title)

        cpu_img = ImageMobject("images/01/cpu.png")
        cpu_img.height=1

        cpu_img.next_to(title, RIGHT)


        code = '''
liste = [4,5,8,3,4,7,6,9]
resultat = []
for i in len(liste):
    resultat[i] = liste[i] ** 2
print(resultat)
    '''.strip()
        rendered_code = Code(code=code, tab_width=4, background="window",
                            language="Python", font="Monospace", style="fruity", line_spacing=0.5)
        self.play(
AddTextWordByWord(
            rendered_code)
            )
        


        
