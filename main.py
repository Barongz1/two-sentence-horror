"""Two-Sentence Horror — entry for make.fun.

Writes two sentences to /output/entry.txt.
The entry is one horror story of exactly two sentences, up to 400 characters.
"""
import os

LINE = "The last thing my smart speaker said before I unplugged it was my own voice, asking it to stay. I never taught it my name, my schedule, or the sound of my breathing in the dark."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
