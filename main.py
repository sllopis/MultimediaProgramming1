# Using type-a synth from pysynth
# 400 notes @ 180 BPM : 15mb wav file

import pysynth as ps
import sys, os
from imagereader import get_column_average
from songmaker import generate_song

file_name = sys.argv[1]
song_name = sys.argv[2]
synth_type = sys.argv[3]
bpm = 200

color_tuples = get_column_average(file_name)
generate_song(color_tuples, song_name, synth_type, bpm)