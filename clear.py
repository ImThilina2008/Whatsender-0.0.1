import glob
import os

pattern = r"Split/*"
for item in glob.iglob(pattern, recursive=True):
    # delete file
    print("Deleting:", item)
    os.remove(item)
pattern = r"Down/*"
for item in glob.iglob(pattern, recursive=True):
    # delete file
    print("Deleting:", item)
    os.remove(item)
os.remove("FileData.py")

import cloud