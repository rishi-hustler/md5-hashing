# MD5 Hash Generator (Menu Driven) – Python

## Overview

This project is a **menu-driven MD5 Hash Generator** implemented in Python.
It demonstrates how the MD5 hashing algorithm can be used for **data integrity verification**, **file hashing**, and **hash comparison** in a cybersecurity context.

The program allows users to generate MD5 hashes for text and files, verify file integrity using known hash values, and compare two MD5 hashes through a simple command-line interface.

---

## Objectives

* Understand how hashing works in cybersecurity
* Learn how MD5 generates a fixed-length hash
* Demonstrate file integrity verification
* Practice secure coding and modular programming in Python
* Build a basic cybersecurity utility suitable for academic use

---

## Features

* Generate MD5 hash for user-provided text
* Generate MD5 hash for any file
* Verify file integrity using a known MD5 hash
* Compare two MD5 hashes
* Menu-driven command-line interface
* Proper error handling for missing files

---

## Technologies Used

* Programming Language: Python 3
* Standard Libraries:

  * `hashlib`
  * `os`

No external libraries are required.

---

## Project Structure

```
MD5-Hash-Generator/
│
├── md5_hash_generator.py
├── README.md
└── sample.txt (optional, for testing)
```

---

## How MD5 Works

* MD5 (Message Digest Algorithm 5) generates a **128-bit hash value**
* The output is always a **32-character hexadecimal string**
* Even a small change in input produces a completely different hash
* MD5 is fast but **not secure against collisions**
* It is suitable for **integrity checks**, not password storage

---

## How to Run the Program

### Step 1: Ensure Python is Installed

Check Python version:

```
python --version
```

### Step 2: Run the Program

```
python md5_hash_generator.py
```

---

## Menu Options Explained

1. **Generate MD5 hash for text**
   Takes a string input and returns its MD5 hash.

2. **Generate MD5 hash for a file**
   Computes the MD5 hash of a file using binary reading.

3. **Verify file integrity using MD5**
   Compares the current file hash with a known hash to detect modification.

4. **Compare two MD5 hashes**
   Checks whether two hash values are identical.

5. **Exit**
   Terminates the program safely.

---

## Sample Use Case

* Store the MD5 hash of an important file
* Recalculate the hash later
* If the hashes differ, the file has been modified or corrupted

---

## Limitations of MD5

* Vulnerable to collision attacks
* Not recommended for password hashing
* Should not be used in modern cryptographic systems

---

## Future Enhancements

* Add SHA-256 and SHA-512 hashing
* Implement password hashing with salt
* Add file integrity monitoring
* Combine multiple algorithms into one tool
* Add logging for audit purposes


