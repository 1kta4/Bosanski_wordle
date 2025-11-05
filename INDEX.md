# Bosanski Wordle - Project Index

## 📁 Project Structure

```
Bosanski_wordle/
├── wordle.py                    # Main game executable
├── words.txt                    # Custom words (created at runtime)
├── stats.json                   # Statistics (created at runtime)
├── requirements.txt             # Python dependencies
├── README.md                    # Main documentation
├── ENHANCEMENT_SUMMARY.md       # What was added/enhanced
├── FEATURES_GUIDE.md           # Complete features walkthrough
└── INDEX.md                     # This file
```

## 📚 Documentation Files

### README.md
**Main documentation file** - Start here!
- Installation instructions
- How to play guide
- Features overview
- Menu options explanation
- Data files description
- Statistics explanation
- Code structure overview
- Requirements

### FEATURES_GUIDE.md
**Complete visual guide** - See exactly what the game looks like
- Main menu visual
- Gameplay examples
- Game feedback display
- Win/lose screens
- Add word workflow
- Statistics display with charts
- Error messages
- Complete gameplay walkthrough
- Technical specifications
- Features checklist

### ENHANCEMENT_SUMMARY.md
**What's new** - Technical overview of enhancements
- New features added
- Function descriptions
- Implementation details
- Data file structures
- Error handling approach
- Backward compatibility notes
- Testing summary
- Usage flow

## 🎮 Main Program: wordle.py

### Core Functions

#### Game Loop & Main
- `main()` - Menu-driven main loop, loads data, handles menu selections
- `play_game(words)` - Play one game, returns (won: bool, attempts: int)

#### Menu System
- `display_menu()` - Shows main menu, returns user choice (1-4)
- `add_word(words)` - Interactive word addition workflow with validation

#### Word Management
- `load_words()` - Loads hardcoded words + custom words from words.txt
- `save_word(word)` - Saves new word to words.txt file

#### Statistics
- `load_stats()` - Loads stats.json or creates default structure
- `save_stats(stats)` - Persists stats dictionary to JSON file
- `update_stats(stats, won, attempts)` - Updates stats after each game
- `display_stats(stats)` - Shows formatted stats with ASCII bar charts

#### Game Logic
- `compare_guess(guess, target)` - Returns [(letter, color), ...] tuples
- `display_colored_word(colored_chars)` - Renders colored letter feedback
- `display_previous_guesses(guesses)` - Shows all previous guesses stacked

#### UI/Display
- `print_box(title, text, width)` - Prints top of unicode box
- `print_box_end(width)` - Prints bottom of unicode box
- `normalize_input(word)` - Converts to lowercase and strips whitespace

### Constants
- `HARDCODED_WORDS` - List of 42 built-in Bosnian words
- `STATS_FILE = "stats.json"` - Statistics file name
- `WORDS_FILE = "words.txt"` - Custom words file name

## 🎮 How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the game
python wordle.py
```

## 🎯 Quick Feature Reference

### Menu Options (1-4)

| Option | Feature | File Used |
|--------|---------|-----------|
| 1 | Play a game | None (uses loaded words) |
| 2 | Add new word | words.txt (append) |
| 3 | View statistics | stats.json (read) |
| 4 | Exit game | - |

### Data Files

| File | Created | Purpose | Format |
|------|---------|---------|--------|
| words.txt | On first custom word | Store player words | Text (UTF-8, one per line) |
| stats.json | On first game | Store game stats | JSON (UTF-8, indent=2) |

## 🔧 Technical Stack

**Language:** Python 3.6+

**Core Libraries:**
- `json` - Statistics serialization
- `os` - File existence checking
- `random` - Word selection

**External Package:**
- `colorama` - Terminal colors and styling

**Color Scheme:**
- Cyan: Borders, menu prompts
- Yellow: Menu options, stats labels
- Green: Success messages, correct letters
- Red: Error messages, loss screen, incorrect letters
- Magenta: Stats headers
- Backgrounds: Green/Yellow/Red for letter feedback

## ✨ Key Features

✅ **Menu-Driven Interface**
- Professional unicode box drawing
- Color-coded options
- Input validation

✅ **Core Game**
- 6 attempts to guess 5-letter word
- Color feedback (green/yellow/red)
- Guess history display

✅ **Word Management**
- 42 built-in Bosnian words
- Add custom words (validated)
- Bosnian character support
- Persistent storage

✅ **Statistics System**
- Total games, wins, losses
- Win percentages
- Win distribution by attempt
- ASCII bar chart visualization

✅ **Data Persistence**
- Automatic file creation
- UTF-8 encoding
- Error recovery
- Cross-session storage

✅ **Professional UX**
- Unicode borders (╔═╗║╚╝╠╣)
- Colored terminal output
- Centered, aligned text
- Clear visual hierarchy

## 🧪 Testing

All features tested and verified:
- ✅ 10/10 test suite passes
- ✅ Menu navigation
- ✅ Word loading and persistence
- ✅ Statistics tracking and display
- ✅ File I/O with error handling
- ✅ UTF-8 Bosnian character support
- ✅ Game logic and color feedback
- ✅ Input validation

## 📊 Statistics Example

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

## 🌍 Bosnian Support

Full UTF-8 support for special characters:
- č (čizme - boots)
- ć (ćirić)
- đ (đokan)
- š (šiška - cone)
- ž (žena - woman)
- dž, lj, nj (digraphs)

## 🚀 Getting Started

1. **Read:** README.md (main guide)
2. **Explore:** FEATURES_GUIDE.md (visual walkthrough)
3. **Run:** `python wordle.py`
4. **Play:** Select option 1 from menu
5. **Customize:** Add words via option 2
6. **Track:** View stats via option 3

## 📝 Version Info

**Current Version:** Enhanced with Menu System, Word Management, Statistics

**Latest Changes:**
- ✨ Menu-driven interface
- ✨ Custom word support
- ✨ Statistics tracking
- ✨ Visual bar charts
- ✨ Professional UI with unicode
- ✨ Data persistence (JSON & text)

## 🎓 Code Quality

- Clean, well-commented code
- Proper error handling
- Input validation throughout
- Function documentation
- Type-clear variable names
- Modular design

## 📞 Support

For detailed information, see:
- **Installation & Setup:** README.md
- **Feature Details:** FEATURES_GUIDE.md
- **Technical Details:** ENHANCEMENT_SUMMARY.md
- **Code Implementation:** wordle.py (inline comments)

---

**Ready to play?** 🎮

```bash
cd Bosanski_wordle
python wordle.py
```

Enjoy! 🇧🇦✨

