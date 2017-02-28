import pysynth as ps

song = (
    ('f', 4), ('e', 4), ('g', 4),
    ('f', 2), ('e', 2), ('g', 2),
    ('f', 3), ('e', 3), ('g', 3),
    ('f', 5)
)

ps.make_wav(song, fn = "song.wav", bpm = 180)