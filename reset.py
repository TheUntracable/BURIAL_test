#This file is used to reset BURIAL, You NEED to run this after each burial use!

import os
import time

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

print("GUI under pogress")
time.sleep(2)
print(f"{BOLD}======================================================================================================================={RESET}")



import shutil
import os

directory_path = "test_files"

if os.path.exists(directory_path):
    shutil.rmtree(directory_path)
    print(f"Directory '{directory_path}' and its contents have been deleted.")
    print("You are now clear to run 'burial.py' again.")
else:
    print(f"Directory '{directory_path}' does not exist.")
