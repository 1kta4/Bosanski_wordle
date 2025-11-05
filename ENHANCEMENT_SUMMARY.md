# Enhanced Bosanski Wordle - Feature Summary

## Overview
The Bosanski Wordle game has been significantly enhanced with a menu system, word management, and comprehensive statistics tracking.

## New Features Added

### 1. Main Menu System
- Replaced simple replay loop with a feature-rich menu
- Unicode box drawing (╔═╗║╚╝╠╣) for professional appearance
- Color-coded menu options using colorama
- Menu options:
  - **Igraj** (Play) - Start a new game
  - **Dodaj novu riječ** (Add Word) - Add custom 5-letter words
  - **Statistike** (Statistics) - View gameplay statistics
  - **Izlaz** (Exit) - Gracefully quit the game

### 2. Word Management System
**Functions Added:**
- `load_words()` - Loads both hardcoded words and custom words from words.txt
- `save_word(word)` - Appends new words to words.txt file
- `add_word(words)` - Interactive word addition with validation

**Features:**
- Validates input: must be exactly 5 letters
- Checks for duplicates (case-insensitive)
- Saves custom words to `words.txt` (UTF-8 encoded)
- Custom words persist across game sessions
- Supports Bosnian special characters

**File Structure:**
```
words.txt
---------
polje
gradski
```

### 3. Statistics & Tracking System
**Functions Added:**
- `load_stats()` - Loads stats from stats.json or creates default structure
- `save_stats(stats)` - Persists statistics to JSON file
- `update_stats(stats, won, attempts)` - Updates stats after each game
- `display_stats(stats)` - Displays formatted statistics with ASCII bar charts

**Tracked Metrics:**
- Total games played
- Total wins and losses
- Win percentage
- Win distribution by attempt (1st try, 2nd try, etc.)

**File Structure (stats.json):**
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

### 4. Enhanced UI/UX
**Visual Improvements:**
- Unicode box drawing for menu and stats displays
- Centered, colored text with Fore.CYAN, Fore.YELLOW, Fore.GREEN, Fore.RED, Fore.MAGENTA
- ASCII bar charts using █ (filled) and ░ (empty) characters
- Organized section headers and clear visual hierarchy

**Display Functions:**
- `print_box(title, text, width)` - Prints top of styled box
- `print_box_end(width)` - Prints bottom of styled box

### 5. Data Persistence
**Implementation Details:**
- **words.txt** - One word per line, UTF-8 encoding, append mode
- **stats.json** - Human-readable JSON with indent=2, UTF-8 encoding

**Error Handling:**
- FileNotFoundError: Creates default stats if file missing
- JSONDecodeError: Recreates stats.json with defaults if corrupted
- Exception handling for all file operations

### 6. Code Structure Changes

**Modified Functions:**
- `play_game(words)` - Now returns tuple `(won: bool, attempts: int)` instead of just bool
  - Takes `words` list as parameter for custom word support

**New Main Loop:**
- `main()` - Completely redesigned for menu-driven operation
  - Loads words and stats at startup
  - Displays menu and handles user choices
  - Updates stats after each game
  - Provides graceful exit

## Technical Implementation

### Standard Library Usage
- `json` - For statistics serialization/deserialization
- `os.path.exists()` - For file existence checking
- `open(encoding='utf-8')` - For UTF-8 file operations
- `random.choice()` - Word selection (existing, reused)

### Color Scheme
- `Fore.CYAN` - Box borders and menu prompts
- `Fore.YELLOW` - Stats labels and menu options
- `Fore.GREEN` - Success messages
- `Fore.RED` - Error messages and stats context
- `Fore.MAGENTA` - Statistics headers
- `Back.GREEN/YELLOW/RED` - Guess feedback (existing)

### File Locations
All files created in the same directory as wordle.py:
- `words.txt` - Custom word storage
- `stats.json` - Statistics storage

## Backward Compatibility
- All original game mechanics preserved
- Core word list unchanged
- Color feedback system intact
- Bosnian character support maintained
- Input validation enhanced but compatible

## Testing Summary
All features tested and verified:
- ✅ Menu navigation
- ✅ Word addition and persistence
- ✅ Statistics tracking and display
- ✅ File I/O with error handling
- ✅ UTF-8 encoding for Bosnian characters
- ✅ JSON serialization/deserialization
- ✅ Game logic integration
- ✅ UI rendering

## Usage Flow

1. **Start Game**
   ```bash
   python wordle.py
   ```

2. **Main Menu Appears**
   ```
   ╔════════════════════════════════════════════════╗
   ║               🎮 BOSANSKI WORDLE                ║
   ╠════════════════════════════════════════════════╣
   
     1. Igraj
     2. Dodaj novu riječ
     3. Statistike
     4. Izlaz
   ```

3. **Player Selects Option**
   - Play: Normal game with statistics tracking
   - Add Word: Input validation, persistence, success confirmation
   - Statistics: View formatted stats with bar charts
   - Exit: Graceful shutdown

## Summary
Enhanced the Bosanski Wordle from a simple CLI game into a feature-complete system with persistent word management and comprehensive gameplay statistics. All changes maintain backward compatibility while providing a professional user experience.

