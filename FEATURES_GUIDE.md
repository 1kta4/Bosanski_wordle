# Bosanski Wordle - Complete Features Guide

## 🎮 Main Menu

When you start the game, you'll see this menu:

```
╔════════════════════════════════════════════════╗
║               🎮 BOSANSKI WORDLE                ║
╠════════════════════════════════════════════════╣

  1. Igraj
  2. Dodaj novu riječ
  3. Statistike
  4. Izlaz

Odaberite opciju (1-4): _
```

## 1️⃣ Play Game (Igraj)

### Gameplay Experience

```
╔════════════════════════════════════════════════╗
║                  🎮 NOVA IGRA                   ║
╠════════════════════════════════════════════════╣

Imate 6 pokušaja da pogodite riječ.
Riječ ima 5 slova.

==============================
Prethodni pokušaji:
==============================
==============================

Pokušaj 1/6: dobar
```

### Guess Feedback

After each guess, you'll see colored feedback:

```
==============================
Prethodni pokušaji:
==============================
Pokušaj 1: D O B A R
==============================

Pokušaj 2/6: slova
```

**Color Legend:**
- 🟩 **GREEN** - Correct letter in correct position
- 🟨 **YELLOW** - Letter exists but wrong position  
- 🟥 **RED** - Letter not in the word

### Win Screen

```
================================
Prethodni pokušaji:
================================
Pokušaj 3: D O B A R
================================

✅ Bravo! Pogodili ste riječ!

================================
```

### Lose Screen

```
================================
Prethodni pokušaji:
================================
Pokušaj 1: S L O V A
Pokušaj 2: T R A V A
Pokušaj 3: K N J I G A
Pokušaj 4: P L A N E T A
Pokušaj 5: M A S K E D
Pokušaj 6: J E D N I M
================================

❌ Kraj igre! Riječ je bila: PRAVI
================================
```

## 2️⃣ Add New Word (Dodaj novu riječ)

Add your own 5-letter Bosnian words to the game!

### Interactive Workflow

```
╔════════════════════════════════════════════════╗
║              ➕ DODAJ NOVU RIJEČ                 ║
╠════════════════════════════════════════════════╣

Unesite novu riječ (ili 'odustani' za povratak): polje
✅ Riječ 'POLJE' uspješno dodana!

╚════════════════════════════════════════════════╝
```

### Error Handling

**Wrong Length:**
```
Unesite novu riječ (ili 'odustani' za povratak): ko
❌ Molimo unesite riječ sa tačno 5 slova.
```

**Duplicate Word:**
```
Unesite novu riječ (ili 'odustani' za povratak): dobar
❌ Riječ 'dobar' već postoji u listi.
```

**Cancel:**
```
Unesite novu riječ (ili 'odustani' za povratak): odustani

╚════════════════════════════════════════════════╝

(Returns to menu)
```

### Word Persistence

Your added words are saved to `words.txt`:
```
polje
gradski
novost
```

Each new word:
- Must be exactly 5 letters
- Can contain Bosnian special characters (č, ć, đ, š, ž)
- Is checked against duplicates (case-insensitive)
- Persists across game sessions
- Appears in the random word selection pool

## 3️⃣ Statistics (Statistike)

View your gameplay statistics with visual charts!

### Statistics Display

```
╔════════════════════════════════════════════════╗
║                  📊 STATISTIKE                  ║
╠════════════════════════════════════════════════╣

Ukupno igara: 10
Pobjeda: 7 (70.0%)
Poraza: 3 (30.0%)

Distribucija pobjeda po pokušaju:

  Pokušaj 1: ██░░░░░░░░░░░░░░░░░░ 14.3% (1)
  Pokušaj 2: █████░░░░░░░░░░░░░░░ 28.6% (2)
  Pokušaj 3: █████░░░░░░░░░░░░░░░ 28.6% (2)
  Pokušaj 4: █████░░░░░░░░░░░░░░░ 28.6% (2)
  Pokušaj 5: ░░░░░░░░░░░░░░░░░░░░ 0.0% (0)
  Pokušaj 6: ░░░░░░░░░░░░░░░░░░░░ 0.0% (0)

╚════════════════════════════════════════════════╝

Pritisnite Enter da se vratite na meni...
```

### Tracked Metrics

**Overall Stats:**
- **Ukupno igara** (Total Games) - All games played
- **Pobjeda** (Wins) - Games won with percentage
- **Poraza** (Losses) - Games lost with percentage

**Win Distribution:**
- Shows how many games won on each attempt (1-6)
- Visual percentage representation
- Count of wins per attempt
- ASCII bar chart with filled (█) and empty (░) blocks

### Statistics File (stats.json)

Automatically created and updated:

```json
{
  "total_games": 10,
  "wins": 7,
  "losses": 3,
  "win_distribution": {
    "1": 1,
    "2": 2,
    "3": 2,
    "4": 2,
    "5": 0,
    "6": 0
  }
}
```

**Statistics Update Logic:**
- After winning: Increments wins and attempt count
- After losing: Increments losses
- Percentages calculated: `(value / total) * 100` with 1 decimal place
- Saved automatically after each game

## 4️⃣ Exit (Izlaz)

```
Odaberite opciju (1-4): 4

👋 Hvala na igranju! Do viđenja!
```

---

## 🌍 Bosnian Character Support

Full support for Bosnian special characters in both game and custom words:

```
č - čizme (boots)
ć - (alternate c with accent)
đ - đokan (gum)
š - šiška (cone)
ž - žena (woman)
dž - džungla (jungle)
lj - ljepota (beauty)
nj - njiše (swings)
```

**Examples in word list:**
- čizme
- nađen
- šiška
- dosje

---

## 💾 Data Files Created

### words.txt
- Location: Same directory as wordle.py
- Format: One word per line
- Encoding: UTF-8
- Purpose: Store player-added custom words
- Example:
  ```
  polje
  gradski
  novost
  ```

### stats.json
- Location: Same directory as wordle.py
- Format: JSON with indent=2 (human-readable)
- Encoding: UTF-8
- Purpose: Persistent storage of game statistics
- Auto-created on first game

---

## 🎮 Complete Gameplay Example

```
$ python wordle.py

╔════════════════════════════════════════════════╗
║               🎮 BOSANSKI WORDLE                ║
╠════════════════════════════════════════════════╣

  1. Igraj
  2. Dodaj novu riječ
  3. Statistike
  4. Izlaz

╚════════════════════════════════════════════════╝

Odaberite opciju (1-4): 1

╔════════════════════════════════════════════════╗
║                  🎮 NOVA IGRA                   ║
╠════════════════════════════════════════════════╣

Imate 6 pokušaja da pogodite riječ.
Riječ ima 5 slova.

==============================
Prethodni pokušaji:
==============================
==============================

Pokušaj 1/6: slova
==============================
Prethodni pokušaji:
==============================
Pokušaj 1: S L O V A
==============================

Pokušaj 2/6: dobar
==============================
Prethodni pokušaji:
==============================
Pokušaj 1: S L O V A
Pokušaj 2: D O B A R
==============================

✅ Bravo! Pogodili ste riječ!
================================

🎮 BOSANSKI WORDLE

  1. Igraj
  2. Dodaj novu riječ
  3. Statistike
  4. Izlaz

Odaberite opciju (1-4): 3

📊 STATISTIKE

Ukupno igara: 1
Pobjeda: 1 (100.0%)
Poraza: 0 (0.0%)

Distribucija pobjeda po pokušaju:

  Pokušaj 1: ░░░░░░░░░░░░░░░░░░░░ 0.0% (0)
  Pokušaj 2: ██████████████████░░ 100.0% (1)
  Pokušaj 3: ░░░░░░░░░░░░░░░░░░░░ 0.0% (0)
  Pokušaj 4: ░░░░░░░░░░░░░░░░░░░░ 0.0% (0)
  Pokušaj 5: ░░░░░░░░░░░░░░░░░░░░ 0.0% (0)
  Pokušaj 6: ░░░░░░░░░░░░░░░░░░░░ 0.0% (0)

Pritisnite Enter da se vratite na meni...

🎮 BOSANSKI WORDLE

  1. Igraj
  2. Dodaj novu riječ
  3. Statistike
  4. Izlaz

Odaberite opciju (1-4): 4

👋 Hvala na igranju! Do viđenja!
```

---

## 🛠️ Technical Specifications

**Language:** Python 3.6+

**Dependencies:**
- colorama (terminal colors)
- Python standard library: json, os, random

**Modules Used:**
- `colorama.Fore` - Text colors
- `colorama.Back` - Background colors  
- `colorama.Style` - Text styling
- `json` - Statistics storage
- `os` - File operations
- `random` - Word selection

**Color Scheme:**
- Menu/Borders: Cyan (Fore.CYAN)
- Options/Labels: Yellow (Fore.YELLOW)
- Success Messages: Green (Fore.GREEN)
- Error Messages: Red (Fore.RED)
- Stats Headers: Magenta (Fore.MAGENTA)
- Guess Feedback: Green/Yellow/Red backgrounds

---

## 📋 Error Handling

**File Operations:**
- Missing stats.json → Creates with default values
- Corrupted stats.json → Recreates with defaults
- File permission errors → Displays user-friendly message

**User Input:**
- Invalid menu choice → Prompts to retry
- Word length ≠ 5 → Shows error, allows retry
- Duplicate word → Alerts user, allows retry
- Invalid game guess → Shows error, no attempt counted

---

## ✨ Features Checklist

- ✅ Menu-driven interface
- ✅ Play games
- ✅ Add custom words
- ✅ View statistics
- ✅ Persistent data storage
- ✅ Unicode box drawing
- ✅ Colored output
- ✅ ASCII bar charts
- ✅ Bosnian character support
- ✅ Error handling
- ✅ Win/loss tracking
- ✅ Win distribution by attempt
- ✅ Percentage calculations
- ✅ UTF-8 file encoding

