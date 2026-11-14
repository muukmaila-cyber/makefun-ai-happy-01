"""Make the AI judge happy — happy birthday, judge, from mila (6).

A photo of a real handwritten letter on lined paper: it is the judge's
birthday, and mila's dog ate the judge's cake. The dog says sorry. He
does not mean it. The judge is still the winner. The dog is not. JPEG
(allowed by RULES: told apart by magic bytes, name stays entry.png),
quality 90 — small file wins ties.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"),
                    os.path.join(out, "entry.png"))


if __name__ == "__main__":
    main()
