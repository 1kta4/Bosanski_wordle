# Bosanski Wordle 🎮

A feature-rich CLI Wordle clone in Python featuring Bosnian words with full support for special characters, word management, and player statistics.

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## How to Play

Run the game:
```bash
python wordle.py
```

You'll be presented with a main menu:
```
╔════════════════════════════════════════════════╗
║               🎮 BOSANSKI WORDLE                ║
╠════════════════════════════════════════════════╣

  1. Igraj
  2. Dodaj novu riječ
  3. Statistike
  4. Izlaz
```

### Menu Options

1. **Igraj (Play)** - Start a new game
2. **Dodaj novu riječ (Add New Word)** - Add custom 5-letter words to the word list
3. **Statistike (Statistics)** - View your gameplay statistics with charts
4. **Izlaz (Exit)** - Quit the game

### Game Rules
- You have **6 attempts** to guess a random 5-letter Bosnian word
- After each guess, letters are colored to show:
  - 🟩 **Green** = correct letter in correct position
  - 🟨 **Yellow** = letter exists in the word but wrong position
  - 🟥 **Red** = letter not in the word

### Features
- ✅ Support for Bosnian special characters (č, ć, đ, š, ž, dž, lj, nj)
- ✅ Case-insensitive input
- ✅ Input validation (only words from the valid list accepted)
- ✅ Colored terminal output with colorama
- ✅ Display of all previous guesses with their color feedback
- ✅ All messages in Bosnian
- ✅ **NEW: Main menu system** with multiple options
- ✅ **NEW: Add custom words** - Save new words to persistent word list
- ✅ **NEW: Statistics tracking** - Track wins, losses, and win distribution
- ✅ **NEW: Visual stats display** - ASCII bar charts showing win statistics

## Data Files

The game creates and manages the following files:

- **words.txt** - Stores custom words added by the player (one per line, UTF-8 encoded)
- **stats.json** - Stores player statistics (JSON format):
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

## Word List

43+ Bosnian words available (42 built-in + custom words):
svime, santa, mukli, ruski, omjer, navod, sitan, dobar, princ, lajav, zulum, zapis, mozak, ispis, ispit, hajka, halka, torta, dosje, nađen, cista, litar, dupke, čizme, fleka, jasen, bunda, mačka, notar, vegan, maska, graja, bonus, kaćun, šiška, prvak, lavić, ameba, repić, struk, dioba, farba, sinoć

### Add Custom Words

Use the "Dodaj novu riječ" menu option to add your own 5-letter words:
1. Select option 2 from the main menu
2. Enter a 5-letter word
3. The word is validated and saved to `words.txt`
4. Your new words persist across game sessions

## Statistics

The game tracks:
- **Total games played**
- **Wins and losses** (with percentage)
- **Win distribution** - How many games were won in 1st, 2nd, 3rd, etc. attempts
- **Visual bar chart** - ASCII visualization of win distribution

View your statistics by selecting option 3 from the main menu.

## Requirements
- Python 3.6+
- colorama (for colored terminal output)
- Standard library modules: json, os, random

## Example Menu Flow

```
╔════════════════════════════════════════════════╗
║               🎮 BOSANSKI WORDLE                ║
╠════════════════════════════════════════════════╣

  1. Igraj
  2. Dodaj novu riječ
  3. Statistike
  4. Izlaz

Odaberite opciju (1-4): 3
```

After selecting Statistics:
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
```

## Code Structure

- `wordle.py` - Main game file containing all game logic and features:
  - **Word Management**
    - `load_words()` - Loads hardcoded and custom words
    - `save_word(word)` - Saves custom words to words.txt
  - **Statistics**
    - `load_stats()` - Loads or creates stats.json
    - `save_stats(stats)` - Persists stats to file
    - `update_stats(stats, won, attempts)` - Updates stats after each game
    - `display_stats(stats)` - Shows formatted statistics with charts
  - **UI & Display**
    - `display_menu()` - Shows main menu
    - `add_word(words)` - Handles word addition workflow
    - `print_box(title, text, width)` - Prints unicode box borders
    - `print_box_end(width)` - Prints box bottom
  - **Game Logic**
    - `compare_guess(guess, target)` - Color-codes letters
    - `display_colored_word(colored_chars)` - Renders colored output
    - `display_previous_guesses(guesses_with_colors)` - Shows guess history
    - `play_game(words)` - Main game loop
    - `main()` - Menu-driven main loop

## License

Feel free to use and modify!

