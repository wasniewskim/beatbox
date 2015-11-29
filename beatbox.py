"""

"""

import warnings
warnings.filterwarnings("ignore")

import create_song
if __name__=='__main__':
    import sys
    print(sys.argv[1])
    create_song.create_song(sys.argv[1])