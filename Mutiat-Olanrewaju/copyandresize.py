import os
import shutil
import glob
from matplotlib import image


def image_resize(image_location, save_location, size):
    # Copy image from one location to another
    for jpgfile in glob.iglob(os.path.join(image_location, "*.jpg")):
        shutil.copy(jpgfile, save_location)

    # Image resizing
    original_image = image.open(image_location)
    width, height = original_image.size
    print('The original image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))
    resized_image = original_image.resize(size)
    width, height = resized_image.size
    print('The resized image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))
    resized_image.show()
    resized_image.save(save_location)


    # Function calling
image_resize(image_location='book.jpg',
             save_location='small_book.jpg', size=(700, 300))
