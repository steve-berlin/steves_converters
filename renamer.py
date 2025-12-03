import subprocess as sp
import os

files = os.listdir("io")
for n in files:
    sp.call(["mv", f"io/{n}", f'io/{n.replace(" ","_")}'])
    print(n.replace(" ", "_"))
