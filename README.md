# yt-dlp_Wrapper
New wrapper for a newer and better maintained fork of yt-download called yt-dlp.<br>
Python modules are not longer sufficent as yt-dlp requires FFMPEG and FFPROBE to transcode videos after download. See the dependencies section for instructions to install the the non-python dependencies.

# Version Notes
This Project is under Active Development. I recommend that you use code from the latest release as the latest commit may be untested and buggy. Releases will be tested before they are published.
<br><br>
Created and tested in Python 3.10.0 on MacOS 13.0.1 running on M1 Sillicon. If you have version related problem please create an issue and include all relavent software versions.

# Dependencies
You must have FFMPEG installed reencode videos during the download. The only working method of installing FFMPEG on my M1 macbook was to use [Homebrew](https://brew.sh/). You can run this command into terminal to do the installation automatically.
``` 
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" 
```
Once Homebrew is installed you should only have to run this command. Note that homebrew requires 10GB of free disk space to install.
```
brew install ffmpeg
```
Currently this script does not automatically install the required python modules, you will have to download them manually.
```
pip install rich
pip install pyperclip
```

# Usage
To use the wrapper, download the file `download.py` from this repo and run it using the terminal command
```
python3 download.py
```
The script will access the clipboard to detect if a YouTube link has already been copied. If so it will use that link for the download. If no YouTube URL is detected it will ask you to paste it into the console.
<br><br>
The Script will then ask if you want to download the linked viedo as a video, audio, or both. 
<br><br>
Finally you will be asked if you want to use a custom filename. Selecting no will let yt-dlp name the file.
The file(s) will be deposited in the same directory that `download.py` is located in.

# Known Limitations/Quirks
1. If you select to download both the Video and Audio the script will download the video twice. There is currently no known way to perform multiple re-encode operations on the same downloaded file.
2. Videos will always be downloaded and converted to .mov files and audio extrations will always be encoded as .wav files. yt-dlp supports a wide range of formats, but this script currently does not give the user the option to change the format.

# Roadmap
- Add argument(s) for selecting different file formats for both Video and Audio - `IN PROGRESS`
- Add argument(s) for downloading playlists
- Add argument(s) for downloading videos in batches via .csv files