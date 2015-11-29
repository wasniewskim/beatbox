"""
modul create_track
stworzennie wektora z czestotliwosciami dla sciezk 
"""

import numpy as np

def create_track(track, defs, samples_dict, inst):
    """
    
    """
    f = open(track, 'r')
    track_matrix = np.array([line.split() for line in f])
    T = len(track_matrix)*60/defs['bpm']
    fs = 44100 
    m = T*fs
    z = np.zeros(m)
    t1 = 60/defs['bpm']
    t = np.linspace(0, t1, t1*fs)
    n = 0
    for i in range(len(track_matrix)):
        for j in range(len(track_matrix[i])):
            temp = track_matrix[i, j]
            if len(temp) == 2:
                if temp != '--':
                    n_s = samples_dict[temp][1]
                    if (n + n_s > len(z)):
                        n_s = m - n
                    z[n:(n + n_s)] += 0.1 * samples_dict[temp][0][:n_s]
            elif len(temp) == 3:
                n_s = fs*t1
                if  temp != "---":
                    z[n:(n + n_s)] += np.sin(2*np.pi*inst[temp[0:2]]*2**(int(temp[2])-4)*t)
        n += fs*60/defs['bpm']
    return z