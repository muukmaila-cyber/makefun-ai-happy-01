"""Make the AI judge happy — a laugh in a letter, from mila (6).

A photo of a real handwritten letter on lined paper: a child gives the
AI judge a laugh in an envelope, because nobody ever makes the judge laugh.
The P.S. lines carry the joke. JPEG (allowed by RULES: told apart by magic
bytes, name stays entry.png), quality 90 — small file wins ties.
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
