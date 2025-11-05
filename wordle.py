#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import json
import os
from colorama import Fore, Back, Style, init

init(autoreset=True)

# Hardcoded word list
HARDCODED_WORDS = [
    "svime", "santa", "mukli", "ruski", "omjer", "navod", "sitan", "dobar",
    "princ", "lajav", "zulum", "zapis", "mozak", "ispis", "ispit", "hajka",
    "halka", "torta", "dosje", "nađen", "cista", "litar", "dupke", "čizme",
    "fleka", "jasen", "bunda", "mačka", "notar", "vegan", "maska", "graja",
    "bonus", "kaćun", "šiška", "prvak", "lavić", "ameba", "repić", "struk",
    "dioba", "farba", "sinoć"
]

STATS_FILE = "stats.json"
WORDS_FILE = "words.txt"

def normalize_input(word):
    """Normalize input to lowercase for comparison."""
    return word.lower().strip()

def print_box(title, text="", width=50):
    """Print a box with centered title and text using unicode."""
    print(Fore.CYAN + "╔" + "═" * (width - 2) + "╗" + Style.RESET_ALL)
    if title:
        centered_title = title.center(width - 2)
        print(Fore.CYAN + "║" + Style.RESET_ALL + centered_title + Fore.CYAN + "║" + Style.RESET_ALL)
    if text:
        print(Fore.CYAN + "║" + Style.RESET_ALL + text.center(width - 2) + Fore.CYAN + "║" + Style.RESET_ALL)
    if title or text:
        print(Fore.CYAN + "╠" + "═" * (width - 2) + "╣" + Style.RESET_ALL)

def print_box_end(width=50):
    """Print bottom of box."""
    print(Fore.CYAN + "╚" + "═" * (width - 2) + "╝" + Style.RESET_ALL)

def load_words():
    """Load words from words.txt and merge with hardcoded list."""
    words = list(HARDCODED_WORDS)
    
    if os.path.exists(WORDS_FILE):
        try:
            with open(WORDS_FILE, 'r', encoding='utf-8') as f:
                custom_words = [line.strip().lower() for line in f if line.strip()]
                for word in custom_words:
                    if word not in words:
                        words.append(word)
        except Exception as e:
            print(Fore.RED + f"❌ Greška pri učitavanju riječi: {e}" + Style.RESET_ALL)
    
    return words

def save_word(word):
    """Append a new word to words.txt."""
    try:
        with open(WORDS_FILE, 'a', encoding='utf-8') as f:
            f.write(word.lower() + '\n')
    except Exception as e:
        print(Fore.RED + f"❌ Greška pri spremanju riječi: {e}" + Style.RESET_ALL)

def load_stats():
    """Load statistics from stats.json or create default structure."""
    default_stats = {
        "total_games": 0,
        "wins": 0,
        "losses": 0,
        "win_distribution": {
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0
        }
    }
    
    if os.path.exists(STATS_FILE):
        try:
            with open(STATS_FILE, 'r', encoding='utf-8') as f:
                stats = json.load(f)
                return stats
        except (json.JSONDecodeError, ValueError):
            return default_stats
        except Exception as e:
            print(Fore.RED + f"❌ Greška pri učitavanju statistike: {e}" + Style.RESET_ALL)
            return default_stats
    
    return default_stats

def save_stats(stats):
    """Save statistics to stats.json."""
    try:
        with open(STATS_FILE, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(Fore.RED + f"❌ Greška pri spremanju statistike: {e}" + Style.RESET_ALL)

def update_stats(stats, won, attempts):
    """Update statistics after a game."""
    stats["total_games"] += 1
    
    if won:
        stats["wins"] += 1
        stats["win_distribution"][str(attempts)] = stats["win_distribution"].get(str(attempts), 0) + 1
    else:
        stats["losses"] += 1
    
    save_stats(stats)
    return stats

def display_stats(stats):
    """Display statistics with formatting and bar charts."""
    print_box("📊 STATISTIKE", width=50)
    print()
    
    total = stats["total_games"]
    wins = stats["wins"]
    losses = stats["losses"]
    win_pct = (wins / total * 100) if total > 0 else 0
    loss_pct = (losses / total * 100) if total > 0 else 0
    
    print(Fore.YELLOW + f"Ukupno igara: " + Style.RESET_ALL + f"{total}")
    print(Fore.GREEN + f"Pobjeda: " + Style.RESET_ALL + f"{wins} ({win_pct:.1f}%)")
    print(Fore.RED + f"Poraza: " + Style.RESET_ALL + f"{losses} ({loss_pct:.1f}%)")
    print()
    
    print(Fore.MAGENTA + "Distribucija pobjeda po pokušaju:" + Style.RESET_ALL)
    print()
    
    distribution = stats["win_distribution"]
    total_wins = wins if wins > 0 else 1
    
    for attempt in range(1, 7):
        attempt_wins = distribution.get(str(attempt), 0)
        attempt_pct = (attempt_wins / total_wins * 100) if total_wins > 0 else 0
        
        # Create bar chart
        bar_length = 20
        filled = int(bar_length * attempt_pct / 100)
        bar = "█" * filled + "░" * (bar_length - filled)
        
        print(f"  Pokušaj {attempt}: {bar} {attempt_pct:.1f}% ({attempt_wins})")
    
    print()
    print_box_end(width=50)
    print()
    input(Fore.YELLOW + "Pritisnite Enter da se vratite na meni..." + Style.RESET_ALL)

def display_menu():
    """Display main menu and return user choice."""
    print_box("🎮 BOSANSKI WORDLE", width=50)
    print()
    
    print(Fore.YELLOW + "  1. " + Style.RESET_ALL + "Igraj")
    print(Fore.YELLOW + "  2. " + Style.RESET_ALL + "Dodaj novu riječ")
    print(Fore.YELLOW + "  3. " + Style.RESET_ALL + "Statistike")
    print(Fore.YELLOW + "  4. " + Style.RESET_ALL + "Izlaz")
    print()
    
    print_box_end(width=50)
    print()
    
    while True:
        choice = input(Fore.CYAN + "Odaberite opciju (1-4): " + Style.RESET_ALL).strip()
        if choice in ['1', '2', '3', '4']:
            return choice
        print(Fore.RED + "❌ Molimo odaberite validnu opciju (1-4)." + Style.RESET_ALL)
        print()

def add_word(words):
    """Handle word addition workflow."""
    print_box("➕ DODAJ NOVU RIJEČ", width=50)
    print()
    
    while True:
        word = input(Fore.CYAN + "Unesite novu riječ (ili 'odustani' za povratak): " + Style.RESET_ALL).strip().lower()
        
        if word == "odustani":
            print()
            return
        
        if len(word) != 5:
            print(Fore.RED + "❌ Molimo unesite riječ sa tačno 5 slova." + Style.RESET_ALL)
            print()
            continue
        
        if word in words:
            print(Fore.RED + f"❌ Riječ '{word}' već postoji u listi." + Style.RESET_ALL)
            print()
            continue
        
        # Valid word - add it
        save_word(word)
        words.append(word)
        print(Fore.GREEN + f"✅ Riječ '{word.upper()}' uspješno dodana!" + Style.RESET_ALL)
        print()
        break
    
    print_box_end(width=50)
    print()

def compare_guess(guess, target):
    """
    Compare guess with target and return color codes for each letter.
    Returns list of tuples: (letter, color)
    Colors: 'green', 'yellow', 'red'
    """
    guess = normalize_input(guess)
    target = normalize_input(target)
    
    result = ['red'] * len(guess)
    target_chars = list(target)
    
    # First pass: mark green (correct position)
    for i, char in enumerate(guess):
        if char == target[i]:
            result[i] = 'green'
            target_chars[i] = None
    
    # Second pass: mark yellow (wrong position)
    for i, char in enumerate(guess):
        if result[i] != 'green' and char in target_chars:
            result[i] = 'yellow'
            target_chars[target_chars.index(char)] = None
    
    return list(zip(guess, result))

def display_colored_word(colored_chars):
    """Display a word with colored backgrounds."""
    color_map = {
        'green': Back.GREEN + Fore.BLACK,
        'yellow': Back.YELLOW + Fore.BLACK,
        'red': Back.RED + Fore.WHITE
    }
    
    output = ""
    for char, color in colored_chars:
        output += color_map[color] + char.upper() + Style.RESET_ALL + " "
    
    return output.strip()

def display_previous_guesses(guesses_with_colors):
    """Display all previous guesses stacked vertically with their colors."""
    print("\n" + "=" * 30)
    print("Prethodni pokušaji:")
    print("=" * 30)
    for i, colored_chars in enumerate(guesses_with_colors, 1):
        word = ''.join([char for char, _ in colored_chars])
        print(f"Pokušaj {i}: {display_colored_word(colored_chars)}")
    print("=" * 30 + "\n")

def play_game(words):
    """Main game loop. Returns (won: bool, attempts: int)."""
    target_word = random.choice(words)
    guesses_with_colors = []
    attempts = 0
    max_attempts = 6
    
    print_box("🎮 NOVA IGRA", width=50)
    print()
    print(Fore.YELLOW + f"Imate {max_attempts} pokušaja da pogodite riječ." + Style.RESET_ALL)
    print(Fore.YELLOW + "Riječ ima 5 slova." + Style.RESET_ALL)
    print()
    
    while attempts < max_attempts:
        display_previous_guesses(guesses_with_colors)
        
        guess = input(f"Pokušaj {attempts + 1}/{max_attempts}: ").strip()
        
        # Validate input
        if len(guess) != 5:
            print("❌ Molimo unesite riječ sa tačno 5 slova.\n")
            continue
        
        guess_normalized = normalize_input(guess)
        if guess_normalized not in words:
            print("❌ Molimo unesite validnu riječ sa liste.\n")
            continue
        
        attempts += 1
        colored_chars = compare_guess(guess, target_word)
        guesses_with_colors.append(colored_chars)
        
        # Check if correct
        if guess_normalized == target_word:
            print("\n" + "=" * 40)
            display_previous_guesses(guesses_with_colors)
            print(Fore.GREEN + "✅ Bravo! Pogodili ste riječ!" + Style.RESET_ALL)
            print("=" * 40 + "\n")
            return (True, attempts)
    
    # Game over - lost
    print("\n" + "=" * 40)
    display_previous_guesses(guesses_with_colors)
    print(Fore.RED + f"❌ Kraj igre! Riječ je bila: {target_word.upper()}" + Style.RESET_ALL)
    print("=" * 40 + "\n")
    return (False, attempts)

def main():
    """Main function with menu loop."""
    words = load_words()
    stats = load_stats()
    
    while True:
        choice = display_menu()
        
        if choice == '1':
            # Play game
            won, attempts = play_game(words)
            stats = update_stats(stats, won, attempts)
            
        elif choice == '2':
            # Add new word
            add_word(words)
            
        elif choice == '3':
            # View statistics
            display_stats(stats)
            
        elif choice == '4':
            # Exit
            print(Fore.GREEN + "👋 Hvala na igranju! Do viđenja!\n" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main()

