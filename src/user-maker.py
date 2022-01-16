try:
    import sys
    import os
    import random
except Exception as e:
    print(e)
    sys.exit()
import colorama
from os import system
system("title " + "Programmed By Lynch - Username List Maker")
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
try:
    Users = int(input(f"[{Fore.GREEN}?{Fore.RESET}] How Many Users Do You Need To Be Made: "))
    Letters = int(input(f"[{Fore.GREEN}?{Fore.RESET}] How Many Letters Does Usernames Contain: "))
except ValueError :
    print(f"[{Fore.RED}!{Fore.RESET}] Only Use Numbers")
    sys.exit()
def Make_users(data):
  Leeter = (Letters)
  User = ""
  while len(User) != Leeter:
    The_Choice = random.choice(data)
    User += The_Choice
  return User
Choose = "qwertyuiopasdfghjklzxcvbnm1234576890"
num = 0
for Make in range(Users):
   Done_User=Make_users(Choose)
   with open('users.txt', 'a+') as Type:
      Type.write(f"{Done_User}\n")
      num += 1
      print(f"\r[{Fore.GREEN}+{Fore.RESET}] Successfully Made >> [{num}] [{Done_User}]", end="")
print("\n+"+"-"*11+"Filtering"+"-"*10+"+")
the_file = open(f'users.txt')
the_lines = the_file.readlines()
the_lines = [line.strip() for line in the_lines]
final_lines = {}
def file_lengthy(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
def file_lengthy2(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
print(f"\r[{Fore.GREEN}+{Fore.RESET}] Before Filtering -->", file_lengthy(f"users.txt"),end="")
for line in the_lines:
    if line not in final_lines.keys():
        final_lines[line] = 0
lines = "\n".join(list(final_lines.keys()))
file = open(f"users.txt", "w")
file.write(lines + "\n")
file.close()
print(f"\n[{Fore.GREEN}+{Fore.RESET}] After Filtering -->", file_lengthy2(f"users.txt"))
print(f"[{Fore.CYAN}i{Fore.RESET}] All Users Were Saved In [ users.txt ]")
⠀ 
