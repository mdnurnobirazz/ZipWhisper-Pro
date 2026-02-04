# ZipWhisper Pro

**ZipWhisper Pro** is a lightweight, fast, and beautiful ZIP password recovery tool written in Python.  
It specializes in **dictionary attacks** (using wordlists like rockyou.txt) and includes an optional brute-force mode for short passwords.

Crack forgotten ZIP passwords quietly and stylishly — like a whisper in the dark... 💕

## Features
- **Dictionary Attack** (primary mode — very fast and effective with good wordlists)
- **Brute-Force Attack** (for short passwords only — 1 to 8 characters recommended)
- Large, colorful ASCII banner for that pro hacker vibe
- Interactive menu with clear options
- Real-time progress bar (thanks to tqdm)
- Automatic file extraction when password is found
- Remembers your last used ZIP file
- Clean error handling and Ctrl+C support
- Works great on **Termux**, Linux, Windows, macOS

## Requirements
- Python 3.8 or higher
- Two Python packages:
  ```bash
  pip install pyzipper tqdm
Installation
1. Clone the repo (recommended)
git clone https://github.com/mdnurnobirazz/ZipWhisper-Pro.git
cd ZipWhisper-Pro
2. Or download only the script
wget https://raw.githubusercontent.com/mdnurnobirazz/ZipWhisper-Pro/main/zip_whisper_pro.py
3. Install dependencies
pip install pyzipper tqdm
Termux users (if Python not installed yet):
pkg update && pkg install python -y
4. Download a powerful wordlist (must for dictionary mode)
wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
(≈140 MB, contains 14+ million common passwords — best starting point)
How to Use
Run the tool:
python zip_whisper_pro.py
You will see a big stylish banner and menu:
[1]  Dictionary Attack (Fast & Recommended)
[2]  Brute-Force Attack (Short passwords only)
[3]  How to Use & Tips
[4]  Exit
Example: Dictionary Attack (most powerful)
Choose 1
Enter ZIP file path → secret.zip
Enter wordlist path → rockyou.txt
Extract files? → Press Enter (default yes)
It will start cracking with a nice progress bar.
If password found → it shows the password and extracts files to extracted/ folder.
Tips & Best Practices
Dictionary > Brute-force — Always start with dictionary mode
Use rockyou.txt or bigger lists from SecLists: https://github.com/danielmiessler/SecLists/tree/master/Passwords
Brute-force only for passwords like 123456 or abcd12 (max 6–8 chars)
Keep ZIP and wordlist in the same folder for easy paths
Termux: Run termux-setup-storage if files are in /sdcard
Legal & Ethical Warning
This tool is for educational and personal use only.
Use it exclusively on ZIP files you own and have forgotten the password for.
Any unauthorized use is illegal and unethical. The author takes no responsibility for misuse.
Contributing
Pull requests are welcome!
Ideas to improve:
Multi-threading for faster dictionary attacks
CLI arguments (argparse support)
More charset presets for brute-force
Auto wordlist downloader
Just open an issue or PR 💕
