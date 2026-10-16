# 🔐 Caesar Cipher Encrypter

A simple command-line tool that encrypts text using the classic Caesar cipher, shifting every letter by a number you choose.

```
===================================
🛡️  CAESAR CIPHER ENCRYPTER  🛡️
===================================
```

## ✨ Features

- Encrypts any message with a custom shift value
- Wraps around the alphabet (`z` + 1 becomes `a`) using modulo 26
- Preserves letter casing (uppercase stays uppercase)
- Keeps spaces, numbers, and special characters unchanged
- Zero dependencies: only Python's standard library

## 🛠 Requirements

- Python 3.6 or newer

## 🚀 Installation

```bash
git clone https://github.com/ka707neki/caesar-cipher.git
cd caesar-cipher
```

## ▶️ Usage

```bash
python3 caesar_cipher.py
```

Then type your message and the shift value when prompted.

### Example

| Message       | Shift | Result        |
|---------------|-------|---------------|
| `Hello World` | 3     | `Khoor Zruog` |
| `xyz`         | 3     | `abc`         |
| `Python 3!`   | 1     | `Qzuipo 3!`   |

> 💡 **Tip:** to decrypt, run the program on the encrypted text with a negative shift (e.g. `-3`).

## 🧠 How it works

1. Each letter is located in the alphabet (`string.ascii_lowercase`).
2. The new position is calculated with `(position + shift) % 26`.
3. If the original letter was uppercase, the result is converted back to uppercase.
4. Anything that is not a letter is added to the output as it is.

## 🗺 Ideas for the future

- [ ] Add a decrypt option to the menu
- [ ] Brute-force mode that tries all 26 shifts
- [ ] Read and write text from files

## 📄 License

Released under the [MIT License](LICENSE).
