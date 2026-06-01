import sys
sys.path.append(r'C:\Users\admin\AppData\Local\Programs\Python\Python314\Lib\site-packages')
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
def aes_cipher(file_path, key_text):
    key_bytes = key_text.encode('utf-8').ljust(32, b'\0')[:32]
    iv = os.urandom(16)

    with open(file_path, 'rb') as f:
        file_data = f.read()

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(file_data) + padder.finalize()

        cipher = Cipher(algorithms.AES(key_bytes),modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    output_file = file_path + '.enc' 
    with open(output_file, 'wb') as f:
        f.write(iv + encrypted_data)
def aes_decryption(file_path, key_text):
    key_bytes = key_text.encode('utf-8').ljust(32, b'\0')[:32]

    with open(file_path, 'rb') as f:
        file_data = f.read()

        iv = file_data[:16]
        actual_encrypted_data = file_data[16:]

    cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded_data = decryptor.update(actual_encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    original_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

    output_file = file_path.replace('.enc', '') + '.decrypted'
    with open(output_file, 'wb') as f:
        f.write(original_data)
if __name__ == "__main__":
    print("---Start Encryption Tool ---")
    print("1.Encrypt File")
    print("2.Decrypt File")
    choice = input("Enter choice (1 or 2): ")

    if choice in ['1' , '2']:
            base_dir  = os.path.dirname(os.path.abspath(__file__))
            file_name = input("Enter file name (e.g. test.txt):").strip()
            target_file = os.path.join(base_dir, file_name)
            secret_key = input("Enter your secret key: ")
    if secret_key:
                if choice == '1' :
                    print("Processing file for encryption...")
                    aes_cipher(target_file, secret_key)
                    print("File encrypted successfully!")
                elif choice == '2':
                    print("Processing file for decryption...")
                    aes_decryption(target_file, secret_key)
                    print("File decrypted successfully!")
else:
            print("File not found")
           