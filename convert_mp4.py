import ffmpeg
import os
import sys

formats = ["wav", "mp3", "m4a", "mkv", "m4b", "ogg", "avi"]

# Set defaults
i = None
o = "mp3"  # default format

if len(sys.argv) > 1:
    i = sys.argv[1]
    if len(sys.argv) > 2:
        o = sys.argv[2]
else:
    i = input("Input mp4 file (without file ending): ")
    o = input(f"Choose an output format (default is mp3): {formats} ") or "mp3"

if o not in formats:
    print("Invalid format, please try again.")
    sys.exit(1)

file_path = f"{i}.mp4"
if os.path.isfile(file_path):
    ffmpeg.input(file_path).output(f"{i}.{o}").run()
else:
    print("Error: file doesn't exist.")
