from PIL import Image
import os

directory = r'DIRECTORY_PATH'
# Change 'DIRECTORY_PATH' to the path of the folder with original images and PyC2.py
extension = "FILE_EXTENSION"
# Change "FILE_EXTENSION" to the extension used in your images
# EG ".png"

for filename in os.listdir(directory):
    if filename.endswith(extension):
        img = Image.open(filename)
        name = (filename)
        cropped = img.crop((L,T,R,B))
        # Chance 'L,T,R,B' to crop dimensions
        # EG '0,90,2880,1710'
        cropped.save(name)
        print(os.path.join(directory, filename))
        continue
    else:
        continue
for filename in os.listdir(directory):
    if filename.endswith(extension):
        img = Image.open(filename)
        img = img.convert("RGB")
        img.save(filename, "JPEG", optimize=True, quality=80)
        # Quality is set to 80 by default
        # Change `optimize=True` to `optimize=False` to disable
        print(os.path.join(directory, filename))
        continue
    else:
        continue
