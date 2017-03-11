import pysynth as psa
import pysynth_b as psb
import pysynth_s as pss
import numpy

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

    for c in data:
        notes_list.append(generate_note(c))

    song = tuple(notes_list)
    ps.make_wav(song, fn = 'uploads/'+name, bpm = beats)
    return (print("Song job finished!"))

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
    if b < 85:
        note = note_types[note_num] + "b" + str(note_octave)
    elif b > 170:
        note = note_types[note_num] + "#" + str(note_octave)
    else:
        note = note_types[note_num] + str(note_octave)

    print(note)
    note_length = round((brightness/765) * 6) + 1
    return((note, note_length))