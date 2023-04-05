from rich.traceback import install
from rich.console import Console
from rich.prompt import Prompt
import pyperclip
import subprocess
import os
install()
c = Console()

def menu(question, choices):
    curNumber = 1
    c.print(question)
    for i in choices:
        c.print(f"{curNumber}. {i}")
        curNumber += 1
    while True:
        usr_input = int(input(">>"))
        if usr_input < 1 or usr_input > len(choices):
            c.print("[-] That Selection is not Valid", style="red")
        else:
            return choices[usr_input - 1]


c.print("[+] Youtube Video Downloader - V2")
clipboard = pyperclip.paste()
clipbaord = "https://www.youtube.com/watch?v=e11hcDhKA1Q" ## REMOVE AFTER TESTING!!
if "youtube" in clipboard or "youtu'be" in clipboard:
    c.print("[+] URL Detected in Clipboard", style="green")
    URL = clipboard
else:
    URL = Prompt.ask("[+] Please Paste the URL you would like to download")

match menu("[+] What would you like to download?", ["Video Only", "Audio Only", "Both"]):
    case "Video Only":
        download_video = True
        download_audio = False
    case "Audio Only":
        download_video = False
        download_audio = True
    case "Both":
        download_video = True
        download_audio = True

command = ['yt-dlp', URL]
if download_video:
    if menu("[+] Do  you want to Convert to .mov?", ["Yes", "No"]) == "Yes":
        command.append("--recode-video")
        command.append("mov")
    if download_audio:
        command.append("-k")
if download_audio:
    command.append("-x")
    command.append("--audio-format")
    command.append("wav")

result = subprocess.call(command)
c.print("[+] Video Download Completge", style="green")
c.print("[-] Checking for junk files")
for file in os.listdir():
    if file.endswith(".webm"):
        c.print(f"[+] Deleting {file}")
        os.remove(file)
c.print("[+] Junk Files Removed...", style="green ")
