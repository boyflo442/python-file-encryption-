# Python File Encryption & Decryption

A desktop Python application with a Tkinter graphical interface for encrypting and decrypting individual files or the files inside a selected folder using AES-based encryption through `pyAesCrypt`.

## Features

- Encrypt a single file
- Decrypt an encrypted `.aes` file
- Encrypt files inside a folder
- Decrypt `.aes` files inside a folder
- Password-protected encryption/decryption
- Simple login and signup interface
- Displays execution time for folder operations
- Tkinter graphical user interface

## Technologies

- Python
- Tkinter
- pyAesCrypt
- PyMySQL (included by the existing signup module)

## Project structure

```text
python-file-encryption/
├── app.py
├── login.py
├── signup.py
├── img1.png
├── img3.png
├── datasheet.example.txt
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup

1. Install Python 3.10+.
2. Clone or download this repository.
3. Create and activate a virtual environment (recommended).
4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Create a local `datasheet.txt` from the example:

```text
Copy datasheet.example.txt to datasheet.txt
```

6. Run the login screen:

```bash
python login.py
```

> `datasheet.txt` is intentionally ignored by Git because it contains local login data. Never commit real passwords or other secrets.

## Security note

This is an educational/portfolio project and is **not intended for production use**. The current authentication implementation stores credentials in a local data file and should be replaced with a proper password-hashing and secure storage system before being used in a real application.

The encryption/decryption functionality should also be tested carefully before using it on important files. Always keep backups of files you encrypt.

## What I learned

This project provided hands-on practice with:

- Python GUI development with Tkinter
- File and directory handling
- Encryption/decryption workflows
- Password-based file protection
- Error/condition handling
- Measuring execution time
- Structuring a small multi-file Python application

## Future improvements

- Replace plain-text credential storage with secure password hashing
- Add proper input validation and error handling
- Use file/folder selection dialogs instead of manual paths
- Add progress indicators for large folders
- Add safer handling for encryption failures so original files are not removed prematurely
- Add automated tests
- Improve the user interface and accessibility
