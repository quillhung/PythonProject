"""
File: blur.py
Name: Quill
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, the original image
    :return: SimpleImage, the blurred image
    """
    # Todo: create a new blank img that is as big as the original one
    new_img = SimpleImage.blank(img.width, img.height)
    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x, y)
            blank_pixel = new_img.get_pixel(x, y)
            blank_pixel.red = img_pixel.red
            blank_pixel.green = img_pixel.green
            blank_pixel.blue = img_pixel.blue

            # red_total = img_pixel.red
            # green_total = img_pixel.green
            # blue_total = img_pixel.blue
            # surrounding_pixels = 1   # including the original pixel

            # blank_pixel.red = img.get_pixel(x, y).red
            # blank_pixel.green = img.get_pixel(x, y).green
            # blank_pixel.blue = img.get_pixel(x, y).blue

            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.
                # blank_pixel.red = img.get_pixel(x+1, y).red+img.get_pixel(x, y+1).red+img.get_pixel(x+1, y+1).red//4
                # blank_pixel.green = img.get_pixel(x+1, y).green+img.get_pixel(x, y+1).green+img.get_pixel(x+1, y+1).green//4
                # blank_pixel.blue = img.get_pixel(x+1, y).blue+img.get_pixel(x, y+1).blue+img.get_pixel(x+1, y+1).blue//4
                right_pixel = img.get_pixel(x+1, y)
                below_pixel = img.get_pixel(x, y+1)
                diag_pixel = img.get_pixel(x+1, y+1)

                blank_pixel.red = blank_pixel.red + right_pixel.red + below_pixel.red + diag_pixel.red // 4
                blank_pixel.green = blank_pixel.green + right_pixel.green + below_pixel.green + diag_pixel.green // 4
                blank_pixel.blue = blank_pixel.blue + right_pixel.blue + below_pixel.blue + diag_pixel.blue // 4

                # red_total += right_pixel.red + below_pixel.red + diag_pixel.red
                # green_total += right_pixel.green + below_pixel.green + diag_pixel.green
                # blue_total += right_pixel.blue + below_pixel.blue + diag_pixel.blue

                # surrounding_pixels = 4

            elif x == img.width-1 and y == 0:
                # Get pixel at the top-right corner of the image.
                left_pixel = img.get_pixel(x-1, y)
                diag_pixel = img.get_pixel(x-1, y+1)
                below_pixel = img.get_pixel(x, y+1)

                red_total += left_pixel.red + diag_pixel.red + below_pixel.red
                green_total += left_pixel.green + diag_pixel.green + below_pixel.green
                blue_total += left_pixel.blue + diag_pixel.blue + below_pixel.blue

                surrounding_pixels = 4

            elif x == 0 and y == img.height-1:
                # Get pixel at the bottom-left corner of the image
                above_pixel = img.get_pixel(x, y-1)
                diag_pixel = img.get_pixel(x+1, y-1)
                right_pixel = img.get_pixel(x+1, y)

                red_total += above_pixel.red + diag_pixel.red + right_pixel.red
                green_total += above_pixel.green + diag_pixel.green + right_pixel.green
                blue_total += above_pixel.blue + diag_pixel.blue + right_pixel.blue

                surrounding_pixels = 4

            elif x == img.width-1 and y == img.height-1:
                # Get pixel at the bottom-right corner of the image
                above_pixel = img.get_pixel(x, y-1)
                diag_pixel = img.get_pixel(x-1, y-1)
                left_pixel = img.get_pixel(x-1, y)

                red_total += above_pixel.red + diag_pixel.red + left_pixel.red
                green_total += above_pixel.green + diag_pixel.green + left_pixel.green
                blue_total += above_pixel.blue + diag_pixel.blue + left_pixel.blue

                surrounding_pixels = 4

            elif 0 < x < img.width-1 and y == 0:
                # Get top edge's pixels (without two corners)
                left_pixel = img.get_pixel(x-1, y)
                right_pixel = img.get_pixel(x+1, y)
                below_left_pixel = img.get_pixel(x-1, y+1)
                below_pixel = img.get_pixel(x, y+1)
                below_right_pixel = img.get_pixel(x+1, y+1)

                red_total += left_pixel.red + right_pixel.red + below_left_pixel.red + below_pixel.red + below_right_pixel.red
                green_total += left_pixel.green + right_pixel.green + below_left_pixel.green + below_pixel.green + below_right_pixel.green
                blue_total += left_pixel.blue + right_pixel.blue + below_left_pixel.blue + below_pixel.blue + below_right_pixel.blue

                surrounding_pixels = 6

            elif 0 < x < img.width-1 and y == img.height-1:
                # Get bottom edge's pixels (without two corners)
                above_left_pixel = img.get_pixel(x-1, y-1)
                above_pixel = img.get_pixel(x, y-1)
                above_right_pixel = img.get_pixel(x+1, y-1)
                left_pixel = img.get_pixel(x-1, y)
                right_pixel = img.get_pixel(x+1, y)

                red_total += above_left_pixel.red + above_pixel.red + above_right_pixel.red + left_pixel.red + right_pixel.red
                green_total += above_left_pixel.green + above_pixel.green + above_right_pixel.green + left_pixel.green + right_pixel.green
                blue_total += above_left_pixel.blue + above_pixel.blue + above_right_pixel.blue + left_pixel.blue + right_pixel.blue

                surrounding_pixels = 6

            elif x == 0 and 0 < y < img.height-1:
                # Get left edge's pixels (without two corners)
                above_pixel = img.get_pixel(x, y-1)
                above_right_pixel = img.get_pixel(x+1, y-1)
                right_pixel = img.get_pixel(x+1, y)
                below_right_pixel = img.get_pixel(x+1, y+1)
                below_pixel = img.get_pixel(x, y+1)

                red_total += above_pixel.red + above_right_pixel.red + right_pixel.red + below_right_pixel.red + below_pixel.red
                green_total += above_pixel.green + above_right_pixel.green + right_pixel.green + below_right_pixel.green + below_pixel.green
                blue_total += above_pixel.blue + above_right_pixel.blue + right_pixel.blue + below_right_pixel.blue + below_pixel.blue

                surrounding_pixels = 6

            elif x == img.width-1 and 0 < y < img.height-1:
                # Get right edge's pixels (without two corners)
                above_pixel = img.get_pixel(x, y-1)
                above_left_pixel = img.get_pixel(x-1, y-1)
                left_pixel = img.get_pixel(x-1, y)
                below_left_pixel = img.get_pixel(x-1, y+1)
                below_pixel = img.get_pixel(x, y+1)

                red_total += above_pixel.red + above_left_pixel.red + left_pixel.red + below_left_pixel.red + below_pixel.red
                green_total += above_pixel.green + above_left_pixel.green + left_pixel.green + below_left_pixel.green + below_pixel.green
                blue_total += above_pixel.blue + above_left_pixel.blue + left_pixel.blue + below_left_pixel.blue + below_pixel.blue

                surrounding_pixels = 6

            else:
                # Inner pixels.
                above_left_pixel = img.get_pixel(x-1, y-1)
                above_pixel = img.get_pixel(x, y-1)
                above_right_pixel = img.get_pixel(x+1, y-1)
                left_pixel = img.get_pixel(x-1, y)
                right_pixel = img.get_pixel(x+1, y)
                below_left_pixel = img.get_pixel(x-1, y+1)
                below_pixel = img.get_pixel(x, y+1)
                below_right_pixel = img.get_pixel(x+1, y+1)

                red_total += above_left_pixel.red + above_pixel.red + above_right_pixel.red + left_pixel.red + right_pixel.red + below_left_pixel.red + below_pixel.red + below_right_pixel.red
                green_total += above_left_pixel.green + above_pixel.green + above_right_pixel.green + left_pixel.green + right_pixel.green + below_left_pixel.green + below_pixel.green + below_right_pixel.green
                blue_total += above_left_pixel.blue + above_pixel.blue + above_right_pixel.blue + left_pixel.blue + right_pixel.blue + below_left_pixel.blue + below_pixel.blue + below_right_pixel.blue

                surrounding_pixels = 9

            blank_pixel.red = red_total // surrounding_pixels
            blank_pixel.green = green_total // surrounding_pixels
            blank_pixel.blue = blue_total // surrounding_pixels

    return new_img


def main():
    """
    This file shows the original image(smiley-face.png) first, and then its blurred image.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
