import os
from os import system
try:
    import requests
except:
    os.system('pip install requests')
import colorama
system("title " + "Programmed By Lynch - Github Checker")
import colorama
from colorama import Fore
colorama.init(autoreset=True)
from time import sleep


logo = """
  _                     _     
 | |   _   _ _ __   ___| |__  
 | |  | | | | '_ \ / __| '_ \ 
 | |__| |_| | | | | (__| | | |
 |_____\__, |_| |_|\___|_| |_|
       |___/                                    
"""

print(Fore.CYAN+logo)
title = ("Made w Love By Lynch, [i]: @l7up")
print(Fore.RED+title)  

input(f"[{Fore.CYAN}i{Fore.RESET}] Press ENTER When You Have [users.txt] File")
u = open("users.txt","r")
z = 0
while 1:
    user = u.readline().split("\n")[0]
    r = requests.get(f"https://github.com/{user}").status_code
    if r == 404:
        print(f"[{Fore.GREEN}+{Fore.RESET}] Available: {user}")
    elif r == 200:
        print(f"[{Fore.RED}-{Fore.RESET}] Not Available: {user}")
    elif r == 406:
            print("Don't Worry")
    else:
        print(f"[{Fore.RED}!{Fore.RESET}] Error, Sats: {r}")

