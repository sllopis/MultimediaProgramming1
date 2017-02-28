import pysynth as ps
import sys, os
from imagereader import get_column_average

color_tuples = get_column_average(sys.argv[1])

for i in range(1,len(color_tuples)):
    print(color_tuples[i])