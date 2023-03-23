# this script sorts .txt, .pdf, .docx, .pptx, .html, .png and .jgp
import os
from pathlib import Path
import shutil

# find default path to downloads
download_path = str(Path.home() / "Downloads")

# verify path with user
print(download_path)
print("Is the 'Downloads' path above correct?")
path_check = input("Enter 'Yes' if correct, 'No' to enter path manually: ")
while path_check.lower() not in ("yes", "no"):
    print("Invalid response, please type 'Yes' or 'No'")
    path_check = input("Enter 'Yes' if correct, 'No' to enter path manually: ")

if path_check.lower() == 'no':
    while True:
        download_path = input("Please enter case-sensitive 'Downloads' path: ")
        if os.path.exists(download_path):
            print("'Downloads' path verified")
            break
        else:
            print("'Downloads' path not verified, try again")

# change to 'Downloads' location
os.chdir(download_path)

# check for directories for files, otherwise make them
if not os.path.exists("Downloaded TXTs"):
    os.makedirs("Downloaded TXTs")
if not os.path.exists("Downloaded PDFs"):
    os.makedirs("Downloaded PDFs")
if not os.path.exists("Downloaded HTMLs"):
    os.makedirs("Downloaded HTMLs")
if not os.path.exists("Downloaded Powerpoints"):
    os.makedirs("Downloaded Powerpoints")
if not os.path.exists("Downloaded Word Docs"):
    os.makedirs("Downloaded Word Docs")
if not os.path.exists("Downloaded Images"):
    os.makedirs("Downloaded Images")

# move files to respective directories by extension
files = os.listdir()
for i in files:
    if i.endswith('.txt'):
        print(os.path.abspath(i))
        old_path = os.path.abspath(i)
        shutil.move(old_path, "Downloaded TXTs")
    elif i.endswith('.pdf'):
        print(os.path.abspath(i))
        old_path = os.path.abspath(i)
        shutil.move(old_path, "Downloaded PDFs")
    elif i.endswith('.html'):
        print(os.path.abspath(i))
        old_path = os.path.abspath(i)
        shutil.move(old_path, "Downloaded HTMLs")
    elif i.endswith('.pptx'):
        print(os.path.abspath(i))
        old_path = os.path.abspath(i)
        shutil.move(old_path, "Downloaded Powerpoints")
    elif i.endswith('.docx'):
        print(os.path.abspath(i))
        old_path = os.path.abspath(i)
        shutil.move(old_path, "Downloaded Word Docs")
    elif i.endswith('.png'):
        print(os.path.abspath(i))
        old_path = os.path.abspath(i)
        shutil.move(old_path, "Downloaded Images")
    elif i.endswith('.jpg'):
        print(os.path.abspath(i))
        old_path = os.path.abspath(i)
        shutil.move(old_path, "Downloaded Images")

print("Sorting Complete!")
