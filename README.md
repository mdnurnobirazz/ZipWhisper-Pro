🔐 ZipWhisper Pro

ZipWhisper Pro is a fast, stylish, and beginner-friendly ZIP password recovery tool built for Termux/Linux environments.
It focuses on high-speed dictionary attacks with optional brute-force mode for short passwords.

Designed to be simple, powerful, and clean — crack your own protected ZIP files like a whisper in the dark.

---

✨ Features

✅ Supports AES + ZipCrypto encrypted ZIPs (via "pyzipper")
✅ Dictionary attack (very fast & recommended)
✅ Optional Brute-force attack
✅ Beautiful colorful banner & interactive menu
✅ Progress bar (tqdm)
✅ Auto extract files when password found
✅ Remembers last used ZIP path
✅ Clean error handling & graceful exit
✅ Works great in Termux / Linux / macOS

---

📸 Preview

ZIPWHISPER PRO
Ultra Fast • Smart • Stylish ZIP Password Recovery Tool
Dictionary Attack - Fast & Powerful

---

⚙️ Installation

1️⃣ Clone the repository

git clone https://github.com/mdnurnobirazz/ZipWhisper-Pro.git
cd ZipWhisper-Pro

2️⃣ Install dependencies

pip install pyzipper tqdm

(Termux users)

pkg update
pkg install python git
pip install pyzipper tqdm

---

🚀 Usage

Run the tool:

python zip_whisper_pro.py

You will see:

[1] Dictionary Attack
[2] Brute-Force Attack
[3] Help
[4] Exit

---

🔥 Attack Modes

🟢 Dictionary Attack (Recommended)

Fastest and most effective method.

Steps:

1. Choose option 1
2. Enter ZIP file path
3. Enter wordlist path
4. Wait for cracking

Example:

secret.zip
rockyou.txt

---

🔴 Brute-Force Attack

Tries all combinations.

⚠️ Slow — use only for short passwords (≤ 6–7 chars)

Steps:

1. Choose option 2
2. Set charset (numbers/letters)
3. Set min/max length

Example:

Charset: 0123456789
Min: 1
Max: 6

---

📚 Wordlist Recommendation

For best results, download rockyou.txt:

wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

This list contains 14M+ real passwords.

---

📂 Output

If password is found:

✔ Password displayed
✔ Files automatically extracted to:

/extracted

---

🧠 Tips for Better Success

✅ Use large wordlists (rockyou, SecLists, etc.)
✅ Dictionary attack first
✅ Avoid brute-force for long passwords
✅ Use SSD for faster reading
✅ Run in Termux/Linux for best performance

---

🛠 Requirements

- Python 3.8+
- pyzipper
- tqdm

---

📁 Project Structure

ZipWhisper-Pro/
│
├── zip_whisper_pro.py
├── README.md
└── wordlists (optional)

---

⚠️ Legal Disclaimer

This tool is created ONLY for educational and recovery purposes.

You must:

✔ Use ONLY on files you own
✔ Have permission to test

❌ Do NOT use for illegal access
❌ Do NOT use for hacking others

The author is not responsible for misuse.

---

❤️ Author

Mdnurnobirazz
GitHub: https://github.com/mdnurnobirazz

Inspired by ethical security research & learning.

---

⭐ Support

If you like this project:

⭐ Star the repo
🍴 Fork it
🛠 Improve it
📢 Share it

---

📜 License

MIT License

Free to use, modify, and distribute.

---

🔐 ZipWhisper Pro — Fast. Clean. Powerful.

Recover your own ZIP files the smart way.
