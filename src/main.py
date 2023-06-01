from manim import *
from pages.C_shaders import S1, S2
from pages.B_maths import M1, M2
from pages.A_pc import PC1, PC2
from pages.A_intro import INTRO
from pages.D_final import F1, F2
import concurrent.futures
import multiprocessing
import os
import shutil
import subprocess

config.disable_caching = False

# 'fourk_quality', 'production_quality', 'high_quality', 'medium_quality', 'low_quality', 'example_quality'
config.quality = "high_quality"

slides = [
    INTRO,
    # PC1,
    # PC2,
    # M1,
    # S1,
    # S2,
    # F1,
    # F2,
]


def render(i):
    slides[i]().render()


# INTRO PC1 PC2 M1 M2 S1 S2

if __name__ == "__main__":
    multiprocessing.freeze_support()
    if os.path.exists("slides"):
        shutil.rmtree(
            "slides")
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
        futures = []
        for i, slide in enumerate(slides):
            futures.append(executor.submit(render, i))
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

    print("manim-slides.exe " + " ".join([s.__name__ for s in slides]))
