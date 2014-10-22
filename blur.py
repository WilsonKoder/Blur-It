__author__ = 'WilsonKoder'

from PIL import Image, ImageFilter
import sys

try:
    original_image = Image.open(str(sys.argv[1]))

    blurred_image = original_image.filter(ImageFilter.GaussianBlur(int(sys.argv[3])))

    original_image.show()
    blurred_image.show()

    blurred_image.save(str(sys.argv[2]))

except:
    print("Blur failed, are you sure you typed in the right file name?")



