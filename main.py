# ai-happy-01 entry (Python 3.13, standard library only).
#
# The image is entry.png beside this file: a golden retriever puppy
# mid-leap through golden autumn leaves, warm golden-hour light, a big
# happy grin, a leaf caught in its mouth. One clear joyful subject, warm
# colours, readable at a glance even small. The program copies it to
# /output/entry.png.
# Deterministic: the same bytes in, the same bytes out, every run.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"), os.path.join(OUT, "entry.png"))
