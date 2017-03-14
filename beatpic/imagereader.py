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

    for x in range(image_width):
        column_color_list = []
        for y in range(image_height):
            pix = img.getpixel((x,y))
            column_color_list.append(pix)
        avg_r = mean(pxl[0] for pxl in column_color_list)
        avg_g = mean(pxl[1] for pxl in column_color_list)
        avg_b = mean(pxl[2] for pxl in column_color_list)
        color_tuples.append((round(avg_r), round(avg_g), round(avg_b)))

    return(color_tuples)
