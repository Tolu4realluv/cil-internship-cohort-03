from PIL import Image
import os, sys
path = ('C:\Users\Amara Obiesie\Pictures\2018-03')
def resize():
for item in os.listdir(path):
    if os.path.isfile(picture):
        im = Image.open(picture)
        f, e = os.path.splitext(picture)
        imResize = im.resize((100,100), Image.ANTIALIAS)
        imResize.save(f + ' resized.jpg', 'JPEG', quality=100)

resize() 