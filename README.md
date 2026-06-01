# AES File Encryption Tool

A secure and lightweight Python-based tool designed to encrypt and decrypt files using the AES-256 algorithm. This project demonstrates practical application of symmetric encryption to protect sensitive data.

## Features
- **AES-256 Encryption:** Uses high-security symmetric encryption.
- **Data Integrity:** Ensures files remain unchanged by creating dedicated `.enc` and `.decrypted` files.
- **Dynamic Path Handling:** Automatically detects file locations, making it portable across different operating systems.
- **User-Friendly:** Simple command-line interface for quick encryption/decryption tasks.

## How to use
1. Run the script using Python: `python encryptor.py`
2. Select your choice (1 for Encrypt, 2 for Decrypt).
3. Enter the file name located in the same directory.
4. Provide your secret key.

## Technical Details
- **Algorithm:** AES (Advanced Encryption Standard).
- **Library:** `cryptography` (hazmat primitives).
- **Padding:** PKCS7 padding for secure data block alignment.

