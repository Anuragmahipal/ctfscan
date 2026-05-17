
# 🛠️ `ctfscan` – BLACKFLAG

> Instant flag finder & decoder for CTFs.  
> Built by [@Anuragmahipal](https://github.com/Anuragmahipal)  
> 🦾 No GUI. No bloat. Just raw shell power.

[![PyPI version](https://badge.fury.io/py/ctfscan.svg)](https://pypi.org/project/ctfscan/)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## ⚔️ What is `ctfscan`?

`ctfscan` is a **blazing-fast terminal utility** for CTF players, reverse engineers, and anyone trying to slice through encoded clues and flag-filled binaries.

📦 Installs in seconds via pip.  
⚡ Runs in a blink.  
🕵️‍♂️ Built for real-world use.

---

## 🔥 Features

| 🔧 Tool        | 📌 Purpose                                |
|---------------|--------------------------------------------|
| `-ff`         | Find `flag{}` / `FLAG{}` / `CTF{}` patterns |
| `-d64`        | Decode base64 data from file               |
| `-dhex`       | Decode hex strings (like shellcode)        |
| `-scan`       | Advanced analysis (exiftool, binwalk, strings) |
| Default mode  | Auto-search for flag-like patterns         |

---

## 🚀 Quick Start

### Installation

**Via pip (recommended):**
```bash
pip install anurag-ctfscan==1.0.1
```

**From source:**
```bash
git clone https://github.com/Anuragmahipal/ctfscan.git
cd ctfscan
pip install -e .
```

**From PYPI:**
```bash
https://pypi.org/project/anurag-ctfscan/1.0.1/
```
### Usage

```bash
# Find all flags recursively
ctfscan -ff secret.txt

# Decode base64
ctfscan -d64 encoded.txt

# Decode hex
ctfscan -dhex shellcode.hex

# Advanced analysis
ctfscan -scan binary_file
```

---

## ⚡ Usage Cheatsheet

```bash
ctfscan -ff <file_or_directory>
# 🔎 Search for flags recursively

ctfscan -d64 <file>
# 📜 Decode base64 content

ctfscan -dhex <file>
# 🧬 Decode hex data

ctfscan -scan <file>
# 🔍 Run exiftool, binwalk, and strings analysis

ctfscan -h
# 📖 Show help
```

---

## 💻 CTF Workflow Integration

Pair `ctfscan` with your favorite tools:

- Grep for flags while solving CTFs
- Decode strings on the fly
- Hex + base64 decoding directly from terminal
- Use in bash scripts and automation
- Integrate with `fzf` and other terminal tools

---

## 🧠 Sample Use Cases

```bash
# Find all flags in a directory:
ctfscan -ff ./capture/

# Decode a file that's base64 encoded:
ctfscan -d64 encoded.txt

# Pipe into another tool:
ctfscan -ff target.bin | tee flags.txt

# Advanced analysis on binary:
ctfscan -scan challenges/binary_challenge
```

---

## ⚙️ Requirements

- Python 3.6 or higher
- Optional: `exiftool`, `binwalk`, `strings` for advanced scanning

---

## 📦 Installation Methods

### Method 1: PyPI (Recommended)
```bash
pip install ctfscan
ctfscan -h
```

### Method 2: From Source
```bash
git clone https://github.com/Anuragmahipal/ctfscan.git
cd ctfscan
pip install -e .
ctfscan -h
```

### Method 3: Development Install
```bash
git clone https://github.com/Anuragmahipal/ctfscan.git
cd ctfscan
pip install -e ".[dev]"
```

---

## 🐛 Troubleshooting

**Command not found after installation?**
- Ensure the pip installation location is in your PATH
- Try: `python -m ctfscan.cli -ff file.txt`

**Optional tools not working?**
- Install: `exiftool`, `binwalk`, `strings`
- On Ubuntu/Debian: `sudo apt-get install exiftool binwalk`
- On macOS: `brew install exiftool binwalk`

---

## 📝 License

MIT License - See [LICENSE](LICENSE) file for details

---

## 🤝 Contributing

Found a bug? Have a feature request?  
Open an issue on [GitHub](https://github.com/Anuragmahipal/ctfscan/issues)

---

## 👨‍💻 Author

**Anuragmahipal**  
GitHub: [@Anuragmahipal](https://github.com/Anuragmahipal)


---

## ☠️ Why Use This?

Because `grep` is noisy. `xxd` is clunky. And most tools aren't built for **CTF pace**.

`ctfscan` is laser-focused, scriptable, minimal, and shell-native.

> Find flags faster. Decode deeper. Hack cleaner. 🧨

---

## 📜 License

MIT — Fork it, enhance it, make it yours.

---

## 👾 Screenshot

```bash
$ ctfscan -ff memory_dump.bin
[+] Found: FLAG{real_binary_capture}
```
