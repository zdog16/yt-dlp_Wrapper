from rich.traceback import install
from rich.console import Console
from rich.prompt import Prompt
import pyperclip
import subprocess
import argparse
install()
c = Console()

def getArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--format", action="store_true", help="Present more file format options")
    args = parser.parse_args()
    return args

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



# MAIN PROGRAM START #
c.print("[+] Youtube Video Downloader - V2")
args = getArguments()
clipboard = pyperclip.paste()
if "youtube" in clipboard or "youtu.be" in clipboard:
    c.print("[+] URL Detected in Clipboard", style="green")
    URL = clipboard
else:
    URL = Prompt.ask("[+] Please Paste the URL you would like to download")

if menu("[+] Would you like to use a custom Filename?", ["Yes", "No"]) == "Yes":
    c.print("[+] Enter the Filename")
    filename = input(">>")
else:
    filename = None

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


if download_video and args.format:
    video_format = menu("[+] Select the File Format for the Video File", ["avi", "flv", "gif", "mkv", "mov", "mp4", "webm"])
else:
    video_format = "mov"
if download_audio and args.format:
    audio_format = menu("[+] Selec the File Format for the Audio File", ["aac", "aiff", "alac", "flac", "m4a", "mka", "mp3", "ogg", "opus", "vorbis", "wav"])
else:
    audio_format = "wav"


if download_video:
    command = ['yt-dlp', URL]
    command.append("--recode-video")
    command.append(video_format)
    if filename != None:
        command.append("-o")
        command.append(filename)
    c.print("[+] Downloading Video...", style="green")
    subprocess.call(command)
if download_audio:
    command = ['yt-dlp', URL]
    command.append("-x")
    command.append("--audio-format")
    command.append(audio_format)
    if filename != None:
        command.append("-o")
        command.append(filename)
    c.print("[+] Downloading Audio...", style="green")
    subprocess.call(command)

if download_audio and download_audio:
    c.print("[+] All Downloads Complete", style="green")
else:
    c.print("[+] Download Complete", style="green")