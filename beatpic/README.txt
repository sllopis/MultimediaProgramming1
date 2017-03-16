PicBeat
CSU:MB - CST 205
3/15/2017
github: https://github.com/sllopis/project2-235
Authors: Daniel Crews, Sergio Llopis Donate, Juan Zuniga Ruiz

Instructions to running PicBeat.
Requires Python 3!
If you have pysynth, numpy, and flask please skip to step 6.
1) Open terminal 
2) Install flask enter: pip install flask
3) Install numpy enter: pip install numpy
4) Instal pysynth:
    a) clone https://github.com/mdoege/PySynth.git
    b) Once it finishes cloning enter: cd PySynth
    c) In the directory enter: python3 setup.py install
5) Then go to the folder project2-235 then cd beatpic.
6) Run run.py enter: python3 run.py
7) Go to your browser and enter: localhost:5000
8) enjoy!

Potential future changes:
It would be nice to do some kind of visualization or at least provide more user feedback.
One example of this could be to have a progress bar that travels across the image as the
song is played.  This would aid the user in seeing the connection between the features of
the image and the notes produced in the song.