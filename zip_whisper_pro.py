#!/usr/bin/env python3
"""
ZipWhisper Pro
Advanced ZIP Password Recovery Tool
Focus: Dictionary Attack (Fast) + Optional Brute-Force

Features:
- Supports AES & ZipCrypto encrypted ZIPs (via pyzipper)
- Multiline colorful banner
- Interactive menu
- Remembers last used ZIP file
- Progress bar with tqdm
- Extract option
- Error handling & graceful exit

Requirements:
pip install pyzipper tqdm

Author: Inspired by @Mdnurnobirazz
License: MIT (or your choice)
"""

import pyzipper
from tqdm import tqdm
import argparse  # Not used now, but can add CLI later
import os
import itertools
import string
import sys
import time

# ANSI Colors for Termux & most terminals
C = lambda text, color_code: f"\033[{color_code}m{text}\033[0m"
GREEN = "32"; RED = "31"; YELLOW = "33"; CYAN = "36"; MAGENTA = "35"; BOLD = "1"

found_password = None
attempts = 0
last_zip_path = None

# Big stylish banner
BANNER = """
╔════════════════════════════════════════════════════════════╗
║                  ZIPWHISPER PRO                           ║
║     Crack ZIP passwords like a whisper in the dark...      ║
║                                                            ║
║   ███████╗██╗██████╗ ██╗    ██╗██╗  ██╗██╗███████╗██████╗  ║
║   ╚══███╔╝██║██╔══██╗██║    ██║██║  ██║██║██╔════╝██╔══██╗ ║
║     ███╔╝ ██║██████╔╝██║ █╗ ██║███████║██║█████╗  ██████╔╝ ║
║    ███╔╝  ██║██╔═══╝ ██║███╗██║██╔══██║██║██╔══╝  ██╔══██╗ ║
║   ███████╗██║██║     ╚███╔███╔╝██║  ██║██║███████╗██║  ██║ ║
║   ╚══════╝╚═╝╚═╝      ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝ ║
║                                                            ║
║   Ultra Fast • Smart • Stylish ZIP Password Recovery Tool  ║
║              Dictionary Attack - Fast & Powerful           ║
╚════════════════════════════════════════════════════════════╝
"""

print(C(BANNER, CYAN + ";" + BOLD))

def try_password(zip_path, password, extract, output_dir):
    global found_password, attempts
    if found_password:
        return False
    try:
        with pyzipper.AESZipFile(zip_path) as zf:
            zf.setpassword(password.encode('utf-8', errors='ignore'))
            if zf.testzip() is None:
                found_password = password
                print(f"\n{C('🎉 PASSWORD FOUND!', GREEN + ';' + BOLD)} {password}")
                if extract:
                    os.makedirs(output_dir, exist_ok=True)
                    zf.extractall(path=output_dir)
                    print(f"{C('📂 Files extracted to:', CYAN)} {output_dir}")
                return True
    except Exception:
        pass  # Silent fail for wrong passwords
    attempts += 1
    return False

def dictionary_crack(zip_path, wordlist_path, extract, output_dir):
    global found_password
    if not os.path.isfile(wordlist_path):
        print(C(f"❌ Wordlist not found: {wordlist_path}", RED))
        return
    print(C(f"Loading wordlist: {wordlist_path}", YELLOW))
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            passwords = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(C(f"Error loading wordlist: {e}", RED))
        return
    print(C(f"Loaded {len(passwords):,} passwords", YELLOW))
    with tqdm(total=len(passwords), desc=C("Cracking", BOLD + ";" + GREEN), unit="pwd", dynamic_ncols=True) as pbar:
        for pwd in passwords:
            if found_password:
                break
            try_password(zip_path, pwd, extract, output_dir)
            pbar.update(1)

def brute_force_crack(zip_path, charset, min_len, max_len, extract, output_dir):
    global found_password
    print(C("\nBrute-force mode (use only for short passwords!)", CYAN))
    total = sum(len(charset) ** length for length in range(min_len, max_len + 1))
    print(C(f"Estimated combinations: {total:,}", YELLOW))
    with tqdm(total=total, desc=C("Brute-forcing", BOLD + ";" + GREEN), unit="pwd", dynamic_ncols=True) as pbar:
        for length in range(min_len, max_len + 1):
            for combo in itertools.product(charset, repeat=length):
                if found_password:
                    break
                pwd = ''.join(combo)
                try_password(zip_path, pwd, extract, output_dir)
                pbar.update(1)

def get_input(prompt, default=None, is_file=False):
    while True:
        val = input(C(prompt, CYAN + ";" + BOLD)).strip()
        if not val and default is not None:
            val = default
        if not val:
            print(C("This field is required!", RED))
            continue
        if is_file and val and not os.path.isfile(val):
            print(C(f"File not found: {val}", RED))
            continue
        return val

def show_menu():
    print("\n" + C("═" * 55, CYAN))
    print(C("              ZIPWHISPER PRO MENU", BOLD + ";" + MAGENTA))
    print(C("═" * 55, CYAN))
    print("  [1]  Dictionary Attack (Fast & Recommended)")
    print("  [2]  Brute-Force Attack (Short passwords only)")
    print("  [3]  How to Use & Tips")
    print("  [4]  Exit")
    print(C("═" * 55, CYAN))
    return input(C("Enter your choice (1-4): ", CYAN + ";" + BOLD)).strip()

def show_help():
    print(C("\nHOW TO USE ZIPWHISPER PRO", BOLD + ";" + YELLOW))
    print("═" * 60)
    print("""
Quick Start:
1. Install dependencies:
   pip install pyzipper tqdm

2. Download a good wordlist (highly recommended):
   wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

3. Run: python zip_whisper_pro.py
   Choose option 1 → Dictionary Attack

Tips:
- Dictionary attack is much faster & effective
- Use rockyou.txt or other large lists for best results
- Brute-force only for passwords ≤ 7-8 characters
- Legal warning: Use ONLY on files you own!

Press Enter to return...
""")
    input()

def main():
    global found_password, attempts, last_zip_path
    print(C("Ready to whisper your ZIP open? 💕", MAGENTA))
    
    while True:
        choice = show_menu()
        
        if choice == "4":
            print(C("\nThank you for using ZipWhisper Pro! 😘", MAGENTA))
            sys.exit(0)
        
        if choice == "3":
            show_help()
            continue
        
        # ZIP path handling
        zip_path = last_zip_path
        if not zip_path or not os.path.isfile(zip_path):
            zip_path = get_input("Enter ZIP file path (e.g. secret.zip): ", is_file=True)
            last_zip_path = zip_path
        
        # Extract option
        extract_input = input(C("Extract files if password found? (y/n, default y): ", CYAN)).strip().lower()
        extract = extract_input in ['', 'y', 'yes']
        output_dir = "extracted" if extract else ""
        
        found_password = None
        attempts = 0
        
        if choice == "1":
            wordlist_path = get_input("Enter wordlist path (e.g. rockyou.txt): ", is_file=True)
            dictionary_crack(zip_path, wordlist_path, extract, output_dir)
        
        elif choice == "2":
            charset = input(C("Charset (default 0123456789): ", CYAN) or "0123456789")
            min_len = int(input(C("Min length (default 1): ", CYAN) or "1"))
            max_len = int(input(C("Max length (default 6): ", CYAN) or "6"))
            brute_force_crack(zip_path, charset, min_len, max_len, extract, output_dir)
        
        else:
            print(C("Invalid choice! Please enter 1-4.", RED))
            continue
        
        if found_password:
            print(C(f"\nSuccess! Password: {found_password}", GREEN + ";" + BOLD))
        else:
            print(C("\nPassword not found in this attempt 😔", RED))
        
        print(C(f"Total attempts: {attempts:,}", YELLOW))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(C("\nStopped by user. See you soon! 🖤", YELLOW))
    except Exception as e:
        print(C(f"Unexpected error: {e}", RED))