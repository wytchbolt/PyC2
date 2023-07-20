### Python Image Crop/Compression Script (PyC2)
A simple script used for batch cropping and compressing image files within a folder.

I wrote this script with the original intent of using it on game screencaps for a CBDQ Twitter bot. MacOS screencaps are, by default, saved as PNGs, and often take up several MBs. Multiply that by a few thousand, and hosting fees add up. Photoshop has a batch action feature, but it's somewhat clunky and slow. This script was written with a somewhat niche usecase in mind, but it works as well for several images as it does for several thousand images.

#### Dependencies
[Pillow](https://pillow.readthedocs.io/en/stable/)

#### Setting up `PyC2.py`
1. Run `pip install Pillow` to install Pillow.

2. Create new folder, and move images and `PyC2.py` into new folder.

3. Change `DIRECTORY_PATH` in `PyC2.py` to the path of the new folder.

#### Usage
1. Change your directory to `DIRECTORY_PATH` with `cd DIRECTORY_PATH`

2. Run PyC2.py with `python3 PyC2.py`

#### Cropping Images
`L,T,R,B` determines the points at which the images will be cropped, in order of left, top, right, bottom.

E.G.: For an image that is 2880x1800, `0,90,2880,1710` would crop 90 pixels from the top and bottom, and 0 pixels from the left and right.

#### Compressing Images
When optimisation is enabled, you can change the quality of the compression. `quality` is set to 80 by default.
