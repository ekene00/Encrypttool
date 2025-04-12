from cryptography.fernet import Fernet
import os

# Generate a new key
def generate_key():
    return Fernet.generate_key()

# Save the key to a file
def save_key(key, filename="secret.key"):
    with open(filename, "wb") as key_file:
        key_file.write(key)

# Load the key from a file
def load_key(filename="secret.key"):
    with open(filename, "rb") as key_file:
        return key_file.read()

# Encrypt a file
def encrypt_file(input_file, output_file, key):
    fernet = Fernet(key)
    with open(input_file, "rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(output_file, "wb") as enc_file:
        enc_file.write(encrypted)
    print(f"File encrypted and saved as '{output_file}'.")

# Decrypt a file
def decrypt_file(input_file, output_file, key):
    fernet = Fernet(key)
    with open(input_file, "rb") as enc_file:
        encrypted = enc_file.read()
    try:
        decrypted = fernet.decrypt(encrypted)
        with open(output_file, "wb") as dec_file:
            dec_file.write(decrypted)
        print(f"File decrypted and saved as '{output_file}'.")
    except Exception as e:
        print("Decryption failed:", e)

# Simple CLI menu
def main():
    print("Text File Encryption/Decryption Tool")
    print("1. Generate and save a new key")
    print("2. Encrypt a file")
    print("3. Decrypt a file")
    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        key = generate_key()
        save_key(key)
        print("New key generated and saved as 'secret.key'.")
    elif choice == "2":
        key_file = input("Enter key filename (default 'secret.key'): ") or "secret.key"
        key = load_key(key_file)
        in_file = input("Enter path to the file to encrypt: ")
        out_file = input("Enter name for the encrypted file (e.g., output.enc): ")
        encrypt_file(in_file, out_file, key)
    elif choice == "3":
        key_file = input("Enter key filename (default 'secret.key'): ") or "secret.key"
        key = load_key(key_file)
        in_file = input("Enter path to the file to decrypt: ")
        out_file = input("Enter name for the decrypted file (e.g., output.txt): ")
        decrypt_file(in_file, out_file, key)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
