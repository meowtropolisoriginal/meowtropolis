# tram28.py 🚋

A Pomodoro timer for the terminal. Lisbon's tram 28 rides from Martim Moniz to Prazeres while you focus.

Coded live in the Meowtropolis video **Lisbon, Portugal — lofi beats to study & code**.

```
  focus #1   12:34
  =================[_28_]-----------------
  next stop: Baixa
```

## Run it

Needs Python 3.8 or newer. No packages to install.

```
python tram28.py            # 25 min focus, 5 min break
python tram28.py 50 10      # 50 min focus, 10 min break
```

Press `Ctrl+C` to stop. The terminal rings a bell when each ride reaches the end of the line.

## Ideas to extend it

- Add a long break after every 4 rides
- Play a sound with `winsound` or `afplay` instead of the terminal bell
- Save how many rides you did each day to a file

---
🐈 Byte travels to a new city every week. See you in the next one.
