"""tram28.py - a Pomodoro timer for the terminal.

Tram 28 rides across Lisbon while you focus.
usage: python tram28.py [focus_min] [break_min]
"""
import sys
import time

STOPS = ["Martim Moniz", "Graça", "Alfama", "Sé",
         "Baixa", "Chiado", "Estrela", "Prazeres"]
TRACK = 40
TRAM = "[_28_]"

# terminal colours
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"
UP = "\033[3F"  # move the cursor up 3 lines


def clock(seconds):
    m, s = divmod(int(seconds), 60)
    return f"{m:02d}:{s:02d}"


def draw(progress, left, label, first=False):
    # where is the tram on the track?
    pos = int(progress * (TRACK - len(TRAM)))
    rail = "=" * pos + TRAM + "-" * (TRACK - len(TRAM) - pos)
    nxt = min(int(progress * (len(STOPS) - 1)) + 1,
              len(STOPS) - 1)
    if not first:
        print(UP, end="")
    print(f"  {CYAN}{label:<10}{RESET} {clock(left)}")
    print(f"  {YELLOW}{rail}{RESET}")
    print(f"  next stop: {STOPS[nxt]:<14}", flush=True)


def ride(minutes, label):
    total = minutes * 60
    start = time.monotonic()
    draw(0, total, label, first=True)
    while (done := time.monotonic() - start) < total:
        draw(done / total, total - done, label)
        time.sleep(0.25)
    draw(1, 0, label)
    print("\a")  # ding! end of the line


def main():
    focus = float(sys.argv[1]) if len(sys.argv) > 1 else 25
    rest = float(sys.argv[2]) if len(sys.argv) > 2 else 5
    print("tram 28 is leaving Martim Moniz...\n")
    rides = 0
    try:
        while True:
            ride(focus, f"focus #{rides + 1}")
            rides += 1
            ride(rest, "break")
    except KeyboardInterrupt:
        print(f"\n{rides} rides today. obrigado!")


if __name__ == "__main__":
    main()
