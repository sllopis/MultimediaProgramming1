# songmaker.py
# Handles the generation and saving of the music files

import pysynth as psa
import pysynth_b as psb
import pysynth_s as pss
import numpy

# generate_song
# data ->       List of tuples.  Each tuple becomes one note
# name ->       What the user would like to call the the song file (filename)
# synth_type -> The type of synthesizer used ('a', 'b', 's')
# beats ->      The beats per minute of the song 
def generate_song(data, name, synth_type, beats):
    if synth_type == 'a':
        ps = psa
    elif synth_type == 'b':
        ps = psb
    elif synth_type == 's':
        ps = pss
    else:
        return (print("Synth type must be 'a', 'b', 's'"))

    notes_list = []

    # For each (R,G,B) tuple, append a note.
    for c in data:
        notes_list.append(generate_note(c))

    # Cast the final note list to a tuple which pysynth expects 
    song = tuple(notes_list)

    # Generate and save the song and return a message to the user once finished
    ps.make_wav(song, fn = 'uploads/'+name + '.wav', bpm = beats)
    return (print("Song job finished!"))

# generate_note
# c -> A tuple with 3 values (R,G,B)
def generate_note(c):
    r = c[0]
    g = c[1]
    b = c[2]
    brightness = sum((r,g,b))

    # Available notes    
    note_types = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
    
    # Note octave created us r and g value.  higher red and green == higher note
    note_octave = round(((r + g) / (255 + 255)) * 7) + 1

    # Note determined by remainder
    note_num = (r + g) % 7

    # Let blue channel determine sharp or flat
    # Also builds the note structed expected by pysynth e.g. (b5, 6)
    if b < 85:
        note = note_types[note_num] + "b" + str(note_octave)
    elif b > 170:
        note = note_types[note_num] + "#" + str(note_octave)
    else:
        note = note_types[note_num] + str(note_octave)

    # Uses the brightness (r+g+b) to determine the length of the note
    note_length = round((brightness/765) * 6) + 1
    return((note, note_length))