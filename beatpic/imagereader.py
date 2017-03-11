from PIL import Image
import os, sys
from statistics import mean

# list for storing average color of each row
def get_column_average(file):
    # Will store the entire list of tuples, the data-type expected by pysynth
    color_tuples = []

    img = Image.open(file)

    # Resize the image down to a maximum of 50x50 to save cpu time and bandwidth
    # May remove or adjust later.
    img.thumbnail((50,50),Image.ANTIALIAS)

    image_width = img.size[0]
    image_height = img.size[1]
    aspectRatio = image_width/image_height

    for x in range(image_width):
        column_color_list = []
        brightest_pixel = 0;
        darkest_pixel = 765;
        for y in range(image_height):
            pix = img.getpixel((x,y))
            if sum(pix) > brightest_pixel:
                brightest_pixel = sum(pix)
            column_color_list.append(pix)
        avg_r = mean(col[0] for col in column_color_list)
        avg_g = mean(col[1] for col in column_color_list)
        avg_b = mean(col[2] for col in column_color_list)
        color_tuples.append((round(avg_r), round(avg_g), round(avg_b), brightest_pixel))

    return(color_tuples)
