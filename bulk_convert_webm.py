import ffmpeg
import os
import sys
from pathlib import Path

formats = ["wav", "mp3", "m4a", "mkv", "m4b", "ogg", "avi", "mp4"]
files = os.listdir("io")
# Set defaults
output = input(f"Choose an output format (default is m4a): {formats} ") or "m4a"
if output not in formats:
    print("Invalid format, please try again.")
    sys.exit(1)
for i in files:
    file_name = Path(f"io/{i}").stem
    file = f"io/{file_name}.webm"
    print(file)
    if os.path.isfile(file):
        ffmpeg.input(file).output(f"io/{file_name}.{output}").run()
    else:
        print("Error: file doesn't exist.")
