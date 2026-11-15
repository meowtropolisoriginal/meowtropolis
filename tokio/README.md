# yamanote.py 🚃

A Pomodoro timer for the terminal. A train loops Tokyo's Yamanote Line while you focus, and every finished focus earns you a haiku.

Coded live in the Meowtropolis video **Tokyo, Japan — lofi to study & code**.

```
  focus #1   12:34
  =================[=JR=]-----------------
  next stop: Shinjuku

  rain on neon signs
  tokyo hums beneath my desk
  a cat on warm books
```

## Run it

Needs Python 3.8 or newer. No packages to install.

```
python yamanote.py            # 25 min focus, 5 min break
python yamanote.py 50 10      # 50 min focus, 10 min break
```

Press `Ctrl+C` to stop. It tells you how many loops you did today.

## Ideas to extend it

- Add your own lines to `FIVE` and `SEVEN` (count the syllables!)
- Save each day's haiku to a file
- Add the other 24 Yamanote stations

---
🐈 Byte travels to a new city every week. See you in the next one.
