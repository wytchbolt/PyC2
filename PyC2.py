from PIL import Image
import os

directory = r'DIRECTORY_PATH'

for filename in os.listdir(directory):
    if filename.endswith(".png"):
        img = Image.open(filename)
        name = (filename)
        cropped = img.crop((L,T,R,B))
        cropped.save(name)
        print(os.path.join(directory, filename))
        continue
    else:
        continue
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        img = Image.open(filename)
        img = img.convert("RGB")
        img.save(filename, "JPEG", optimize=True, quality=80)
        print(os.path.join(directory, filename))
        continue
    else:
        continue
