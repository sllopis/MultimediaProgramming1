from PIL import Image
import os, sys
from statistics import mean

# list for storing average color of each row
def get_column_average(file):
    color_tuples = []

    img = Image.open(file)

    imageWidth = img.size[0]
    imageHeight = img.size[1]

    for x in range(imageWidth):
        column_color_list = []
        for y in range(imageHeight):
            pix = img.getpixel((x,y))
            column_color_list.append(pix)
        avg_r = mean(col[0] for col in column_color_list)
        avg_g = mean(col[1] for col in column_color_list)
        avg_b = mean(col[2] for col in column_color_list)
        color_tuples.append((round(avg_r), round(avg_g), round(avg_b)))

    return(color_tuples)
