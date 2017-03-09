# Using type-a synth from pysynth
# 400 notes @ 180 BPM : 15mb wav file

import pysynth as ps
import sys, os
from imagereader import get_column_average

color_tuples = get_column_average(sys.argv[1])
notes_list = []

note_types = ('a', 'b', 'c', 'd', 'e', 'f', 'g')

for c in color_tuples:
    note_num = c[0]%6
    note = note_types[note_num]
    octave = (c[1]%7) + 1
    notes_list.append((note, octave))

#for note in notes_list:
#   print(note)



song = tuple(notes_list)

ps.make_wav(song, fn = str(sys.argv[2]), bpm = 180)



