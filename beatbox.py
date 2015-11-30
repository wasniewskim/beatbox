#!python
"""
beatbox - main aplication

create .wav file 
"""
import create_song
import sys
import warnings
warnings.filterwarnings("ignore")

song = sys.argv[1]
if song[-1:] == '/':
    song = song[:-1]


x  = create_song.create_song(song)
if (x == None):
	print(song + ".wav")
else: 
	print(x)