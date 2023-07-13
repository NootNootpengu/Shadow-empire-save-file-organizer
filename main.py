import os
import shutil
from colorama import Fore as fore
import string
import time

def set_folder(save_folder):
    try:
        os.chdir(save_folder)
    except:
        print(fore.RED + "\n[-] Failed to set folder, please send error to https://github.com/NootNootpengu/Shadow-empire-save-file-organizer\n")
        raise
    
    

def start_up():
    os.system('cls')
    print("[+] Starting program, please wait.")
    time.sleep(1)
    os.system('cls')
    print("[+] Starting program, please wait..")
    time.sleep(1)
    os.system('cls')
    print("[+] Starting program, please wait...")
    time.sleep(1)
    os.system('cls')
    print("[+] Starting program, please wait.")
    time.sleep(1)
    os.system('cls')
    print("[+] Starting program, please wait..")
    time.sleep(1)
    os.system('cls')
    print("[+] Starting program, please wait...")
    time.sleep(1)
    os.system('cls')

def main():
    files = os.listdir()
    for file in files:
        file_name = file.lower()
        if file_name.startswith("pbem") and file_name.endswith(".se1"):
            print(fore.BLUE + f"[+] {file} is a PBEM shadow empire file.")
            game_num = file_name.replace(".se1", "")
            game_num = ''.join(e for e in game_num if e.isalnum())
            remove_letters = str.maketrans('', '', string.ascii_letters)
            res = game_num.translate(remove_letters)
            try:
                dir_name = f'PBEM{res}'
                os.mkdir(dir_name)
            except FileExistsError as exist:
                print(exist)
                pass
            shutil.copy(file, dir_name)
            os.remove(file)
            print(fore.LIGHTBLUE_EX + f'[+] Successfully copied {file} to {dir_name}')
        else:
            print(fore.RED + f"[-] {file} is not a PBEM shadow empire file.")
        





if __name__ == "__main__":
    set_folder(save_folder=input("Please enter your folders path containing saves: "))
    start_up()
    main()
    print('')
    print(fore.YELLOW + "Thank you for using our program, please leave a review at our github page:\nhttps://github.com/NootNootpengu/Shadow-empire-save-file-organizer\n")
    input("press enter to exit...\n")





