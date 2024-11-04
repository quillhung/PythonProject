"""
File: fire.py
Name: Quill
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: images/greenland-fire.png
    :return: highlighted_fire
    """
    highlighted_fire = SimpleImage('images/greenland-fire.png')
    for pixel in highlighted_fire:
        avg = (pixel.red+pixel.green+pixel.blue)//3
        if pixel.red < avg*HURDLE_FACTOR:   # gray scale
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
        else:   # highlight the red area (fire area)
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
    return highlighted_fire


def main():
    """
    :param img: SimpleImage, the original image.
    :return: SimpleImage, the updated image with all pixels turning gray except fire area.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
