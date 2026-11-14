"""Make the AI judge happy — happy birthday, judge, from mila (6).

A photo of a real handwritten letter on lined paper: nobody wrote the
judge's birthday down anywhere, so mila asked the calendar. It said
today. She drew the judge a cake and decided that today the judge is
the winner. JPEG (allowed by RULES: told apart by magic bytes, name
stays entry.png), quality 90 — small file wins ties.
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
