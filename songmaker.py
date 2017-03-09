import pysynth as psa
import pysynth_b as psb
import pysynth_s as pss
import numpy

def generate_song(data, name, synth_type, bpm):
    if synth_type == 'a':
        ps = psa
    elif synth_type == 'b':
        ps = psb
    elif synth_type == 's':
        ps = pss
    else:
        return (print("Synth type must be 'a', 'b', 's'"))

    notes_list = []
    note_types = ('a', 'b', 'c', 'd', 'e', 'f', 'g')

    for c in data:
        note_num = c[0]%6
        note = note_types[note_num]
        octave = (c[1]%7) + 1
        notes_list.append((note, octave))

    song = tuple(notes_list)
    ps.make_wav(song, fn = name, bpm = 300)
    return ("Song finished!")