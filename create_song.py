"""
modul create_song

tworzy plik .vaw 
"""
import numpy as np
import scipy 
import scipy.io.wavfile
import scipy.signal
import os
import os.path
import zipfile
import create_track as ct

def create_song(song):
    """
    create track 
    Arguments:
        * song - dictionary or .zip file with song definition 
    """

    if os.path.exists(song):
        song_path = song + "/"
    elif zipfile.is_zipfile(song + ".zip"):
        song_zip = zipfile.ZipFile(song + '.zip')
        song_zip.extractall("/tmp/")
        song_path = "/tmp/" + song + "/"
    else:
        return "There's no such song definition"

    defs = open(song_path + 'defs.txt', 'r').read()
    defs = eval(defs)
    
    sample = [f for f in os.listdir(song_path) if f.endswith(".wav")]
    samples_dict = {}
    for si in sample:
        x = scipy.io.wavfile.read(song_path+si)[1]
        if len(np.shape(x)) > 1:
            x = np.mean(x,axis=1)
        samples_dict[si[6:8]] = x/max(np.abs(x)), np.shape(x)[0]
    

    S = pow(2,1/12)
    m = ["C-", "C#", "D-", "D#", "E-", "F-", "F#", "G-", "G#", "A-", "A#", "B-"]
    f = [440*S**(i-9) for i in range(12)]
    inst = {m[i]:f[i] for i in range(len(m))}
    
    tracks = [f for f in os.listdir(song_path) if f.find("track")>=0]
    tracks_dict = {}
    for t in tracks:
        x = ct.create_track(song_path + t, defs, samples_dict, inst) 
        tracks_dict[t[5:7]] = x 
	


    f_song = open(song_path + '/song.txt', 'r')
    t = np.array([line for line in f_song])
    y = np.array([])
    for tr in t:
        y = np.r_[y, tracks_dict[tr[0:2]]]
        
    scipy.io.wavfile.write(song + '.wav',
                       44100,
                       np.int16(y/max(np.abs(y))*32767))