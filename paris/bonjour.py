"""bonjour.py - French flashcards for the terminal.

A French word appears, then its meaning and an example.
Learn a little French while you study.
usage: python bonjour.py [seconds_per_side]
"""
import random
import sys
import time

# French, English, an example sentence
CARDS = [
    ("le chat", "the cat", "Le chat dort ici."),
    ("la pluie", "the rain", "J'aime la pluie."),
    ("la fenêtre", "the window", "Paris, ma fenêtre."),
    ("le livre", "the book", "Un bon livre."),
    ("étudier", "to study", "J'étudie le soir."),
    ("la nuit", "the night", "La nuit tombe."),
    ("le café", "the coffee", "Un café, merci."),
    ("le croissant", "croissant", "Il est chaud !"),
    ("le toit", "the roof", "Les toits sont gris."),
    ("la tour", "the tower", "Elle brille."),
    ("une pause", "a break", "On fait une pause ?"),
    ("doucement", "slowly, gently", "Parle doucement."),
    ("l'étoile", "the star", "Une étoile brille."),
    ("le calme", "the calm", "Le calme du soir."),
    ("apprendre", "to learn", "On apprend un peu."),
    ("bonne nuit", "good night", "Bonne nuit, Byte."),
]

# terminal colours
BLUE = "\033[34m"
PINK = "\033[35m"
GREY = "\033[90m"
RESET = "\033[0m"


def show(card, number, wait):
    word, meaning, example = card
    print(f"  {GREY}card {number}{RESET}")
    print(f"  {BLUE}{word}{RESET}", flush=True)
    time.sleep(wait)  # try to guess before the answer
    print(f"  = {PINK}{meaning}{RESET}")
    print(f"  {GREY}{example}{RESET}\n", flush=True)
    time.sleep(wait)


def main():
    wait = float(sys.argv[1]) if len(sys.argv) > 1 else 8
    deck = CARDS[:]
    seen = 0
    print("bonjour! a little French while you study.\n")
    try:
        while True:
            random.shuffle(deck)
            for card in deck:
                seen += 1
                show(card, seen, wait)
    except KeyboardInterrupt:
        print(f"\n{seen} cards today. à bientôt!")


if __name__ == "__main__":
    main()
