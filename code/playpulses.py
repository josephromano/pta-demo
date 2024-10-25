import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write, read

def playpulses(filename):

    '''
    play recorded sound that was saved to .txt file;
    the time-series data is returned as a [Ntx2] array ts
    '''
    
    # first construct wavfile
    ts = np.loadtxt(filename)
    audio_data = ts[:,1]
    ##sample_rate = 44100
    sample_rate = 22050
    
    # Playback the audio
    print("playing back...")
    sd.play(audio_data, sample_rate)
    sd.wait() # wait for playback to finish
    print("playback finished")

    return ts
