[README_caesar_full.md](https://github.com/user-attachments/files/33550591/README_caesar_full.md)
# 🔐 Caesar Cipher Toolkit

Two small command-line tools in Python: one **encrypts** text with the classic Caesar cipher, and the other **decrypts** it back when you know the shift.

```
===================================
🛡️  CAESAR CIPHER ENCRYPTER  🛡️
===================================
```

## ✨ Features

- Encrypt and decrypt messages with a custom shift value
- Wraps around the alphabet (`z` + 1 becomes `a`) using modulo 26
- Preserves letter casing (uppercase stays uppercase)
- Keeps spaces, numbers, and special characters unchanged
- Zero dependencies: only Python's standard library

## 📁 Structure

```
caesar-cipher/
├── caesar_cipher.py     # encrypt a message
├── caesar_decrypt.py    # decrypt a message
└── README.md
```

## 🛠 Requirements

- Python 3.6 or newer

## 🚀 Installation

```bash
git clone https://github.com/ka707neki/caesar-cipher.git
cd caesar-cipher
```

## ▶️ Usage

**Encrypt:**
```bash
python3 caesar_cipher.py
```

**Decrypt:**
```bash
python3 caesar_decrypt.py
```

Each tool asks for a message and a shift number.

### Example

| Tool    | Message       | Shift | Result        |
|---------|---------------|-------|---------------|
| Encrypt | `Hello World` | 3     | `Khoor Zruog` |
| Decrypt | `Khoor Zruog` | 3     | `Hello World` |
| Encrypt | `xyz`         | 3     | `abc`         |
| Encrypt | `Python 3!`   | 1     | `Qzuipo 3!`   |

## 🧠 How it works

1. Each letter is located in the alphabet (`string.ascii_lowercase`).
2. **Encrypt:** new position = `(position + shift) % 26`.
   **Decrypt:** new position = `(position - shift) % 26`.
3. If the original letter was uppercase, the result is converted back to uppercase.
4. Anything that is not a letter is added to the output as it is.

## 🗺 Ideas for the future

- [ ] Brute-force mode that tries all 26 shifts when the shift is unknown
- [ ] One menu to choose between encrypt and decrypt
- [ ] Read and write text from files

## 📄 License

Released under the [MIT License](LICENSE).
