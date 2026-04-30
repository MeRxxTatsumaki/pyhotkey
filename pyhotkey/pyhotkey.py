import os
import time
import sys
print("Kurulum başladı 😎")

os.system("sudo apt install python3 python3-tk -y")

aliases = """
alias clox='xclock'
alias pg='python3 -m idlelib'
alias pt='python3 -m tkinter'
alias py='python3'
alias p-cmds='echo Komutlar: pg, pt, py'
"""

os.system(f'echo "{aliases}" >> ~/.bashrc')

print("Kurulum bitti 🎉")
print("Terminale 'p-cmds' yazarak komutları görebilirsin 3 saniye sonra kurulum bittiği için kurulum penceresi kapanacak")

time.sleep(3)
sys.exit()
