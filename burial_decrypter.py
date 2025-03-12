import os
import time
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

# Define ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

BOLD = "\033[1m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
REVERSE = "\033[7m"
STRIKETHROUGH = "\033[9m"

# Function to display a fancy loading animation
def loading_animation(duration):
    symbols = ["/", "-", "\\", "|"]
    end_time = time.time() + duration
    while time.time() < end_time:
        for symbol in symbols:
            sys.stdout.write(f"\rDecrypting... {BOLD}{YELLOW}{symbol}{RESET}")
            sys.stdout.flush()
            time.sleep(0.1)
    print()

# Function to decrypt files in a directory
def decrypt_files(directory, key):
    try:
        fernet = Fernet(key)
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                print(f"{CYAN}Decrypting file: {file_path}{RESET}")

                with open(file_path, "rb") as f:
                    encrypted_data = f.read()

                # Decrypt the data
                decrypted_data = fernet.decrypt(encrypted_data)

                # Save the decrypted data back to the file
                with open(file_path, "wb") as f:
                    f.write(decrypted_data)
                print(f"{GREEN}File decrypted: {file_path}{RESET}")
        return True  # Decryption succeeded
    except Exception as e:
        print(f"{RED}FAILED: Decryption failed. The key may be incorrect.{RESET}")
        return False  # Decryption failed

# Main function
def main():
    # Define the directory to unlock
    target_directory = "test_files"  # Replace with the directory containing the locked files

    print("             ")
    print("             ")
    print(f"{YELLOW}                                    Welcome to the File Decryptor!                 {BLINK}{BLUE}v.1.0 pre-release{RESET}")
    print("             ")
    print(f"{STRIKETHROUGH}================================================================================================================={RESET}")
    time.sleep(2)

    while True:
        # Ask the user for the key (from email)
        key_input = input(f"{YELLOW}Enter the key (from your email) or type 'quit' to exit: {RESET}").strip()

        # Check if the user wants to quit
        if key_input.lower() == "quit":
            print(f"{RED}Exiting...{RESET}")
            time.sleep(2.4)
            break

        # Convert the key to bytes
        try:
            key = key_input.encode()  
        except Exception as e:
            print(f"{RED}Invalid key format. Please try again.{RESET}")
            continue

        # Decrypt the files
        print(f"{YELLOW}Starting decryption process...{RESET}")
        loading_animation(3)  

        if decrypt_files(target_directory, key):
            print(f"{GREEN}Decryption process completed successfully!{RESET}")
            break 
        else:
            print(f"{RED}Decryption failed. Please try again or type 'quit' to exit.{RESET}")

if __name__ == "__main__":
    main()
