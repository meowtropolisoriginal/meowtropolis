"""yamanote.py - a Pomodoro timer for the terminal.

A train loops Tokyo's Yamanote Line while you focus.
Every finished focus earns you a haiku.
usage: python yamanote.py [focus_min] [break_min]
"""
import random
import sys
import time

STATIONS = ["Tokyo", "Ueno", "Ikebukuro",
            "Shinjuku", "Shibuya", "Shinagawa"]
TRACK = 40
TRAIN = "[=JR=]"

# haiku parts: 5 syllables, then 7, then 5
FIVE = ["rain on neon signs",
        "the last train departs",
        "a cat on warm books",
        "steam from a tea cup",
        "quiet keyboard clicks",
        "lanterns in the rain"]
SEVEN = ["tokyo hums beneath my desk",
         "one more line of code compiles",
         "neon lights blink back at me",
         "the green train circles the night",
         "tea goes cold, the bug remains"]

# terminal colours
GREEN = "\033[32m"
CYAN = "\033[36m"
PINK = "\033[35m"
RESET = "\033[0m"
UP = "\033[3F"  # move the cursor up 3 lines


def haiku():
    # two different short lines around a long one
    first, last = random.sample(FIVE, 2)
    return [first, random.choice(SEVEN), last]


def clock(seconds):
    m, s = divmod(int(seconds), 60)
    return f"{m:02d}:{s:02d}"


def draw(progress, left, label, first=False):
    pos = int(progress * (TRACK - len(TRAIN)))
    rest = TRACK - len(TRAIN) - pos
    rail = "=" * pos + TRAIN + "-" * rest
    # the line is a loop: after Shinagawa comes Tokyo
    n = len(STATIONS)
    nxt = STATIONS[min(int(progress * n) + 1, n) % n]
    if not first:
        print(UP, end="")
    print(f"  {CYAN}{label:<10}{RESET} {clock(left)}")
    print(f"  {GREEN}{rail}{RESET}")
    print(f"  next stop: {nxt:<12}", flush=True)


def ride(minutes, label):
    total = minutes * 60
    start = time.monotonic()
    draw(0, total, label, first=True)
    while (done := time.monotonic() - start) < total:
        draw(done / total, total - done, label)
        time.sleep(0.25)
    draw(1, 0, label)
    print("\a")  # ding! back at Tokyo station


def main():
    focus = float(sys.argv[1]) if len(sys.argv) > 1 else 25
    rest = float(sys.argv[2]) if len(sys.argv) > 2 else 5
    print("the Yamanote Line is leaving Tokyo...\n")
    loops = 0
    try:
        while True:
            ride(focus, f"focus #{loops + 1}")
            loops += 1
            for line in haiku():
                print(f"  {PINK}{line}{RESET}")
            print()
            ride(rest, "break")
    except KeyboardInterrupt:
        print(f"\n{loops} loops today. arigatou!")


if __name__ == "__main__":
    main()
