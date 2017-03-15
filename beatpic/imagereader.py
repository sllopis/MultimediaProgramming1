# imagereader.py
# Handles the collection of color data from an image

from PIL import Image
import os, sys
from statistics import mean

# get_column_average
# file -> The absolute path of the file
# Returns a list of tuples based on the average rgb value of each
def get_column_average(file):
    # Will store the entire list of tuples, the data-type expected by pysynth
    color_tuples = []

    img = Image.open(file)

    # Resize the image down to a maximum of 50x50 to save cpu time and bandwidth
    img.thumbnail((50,50),Image.ANTIALIAS)

    # Gather the height and width of the resized image
    image_width = img.size[0]
    image_height = img.size[1]

    # Nested for loops to access each pixel
    for x in range(image_width):
        column_color_list = [] # One column's worth of tuples (R,G,B)
        
        # Gets each pixel (x,0) to (x,image_height) and adds it to the list for the column
        for y in range(image_height):
            pix = img.getpixel((x,y))
            column_color_list.append(pix)
        
        # Obtains the average (R,G,B) for the entire column and appends it to
        # the list to be returned
        avg_r = mean(pxl[0] for pxl in column_color_list)
        avg_g = mean(pxl[1] for pxl in column_color_list)
        avg_b = mean(pxl[2] for pxl in column_color_list)
        color_tuples.append((round(avg_r), round(avg_g), round(avg_b)))

    return(color_tuples)
