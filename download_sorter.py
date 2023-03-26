# this script sorts .txt, .pdf, .docx, .pptx, .html, .png and .jgp
import os
from pathlib import Path
import shutil

#use tuples for folders with multiple file extensions 
document_ext = (".txt", ".pdf", ".docx", ".doc")
image_ext = (".jpg", ".png", ".gif")
powerpoint_ext = (".pptx", ".pptm", ".ppt")

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
if not os.path.exists("Downloaded Documents"):
    os.makedirs("Downloaded Documents")
if not os.path.exists("Downloaded Images"):
    os.makedirs("Downloaded Images")
if not os.path.exists("Downloaded HTMLs"):
    os.makedirs("Downloaded HTMLs")
if not os.path.exists("Downloaded Powerpoints"):
    os.makedirs("Downloaded Powerpoints")

# move files to respective directories by extension
files = os.listdir()
for file in files:
    if file.endswith(document_ext):
        #print(os.path.abspath(file))
        old_path = os.path.abspath(file)
        shutil.move(old_path, "Downloaded Documents")
    elif file.endswith(image_ext):
        #print(os.path.abspath(file))
        old_path = os.path.abspath(file)
        shutil.move(old_path, "Downloaded Images")    
    elif file.endswith(powerpoint_ext):
        #print(os.path.abspath(file))
        old_path = os.path.abspath(file)
        shutil.move(old_path, "Downloaded Powerpoints")
    elif file.endswith('.html'):
        #print(os.path.abspath(file))
        old_path = os.path.abspath(file)
        shutil.move(old_path, "Downloaded HTMLs")

print("Sorting Complete!")
