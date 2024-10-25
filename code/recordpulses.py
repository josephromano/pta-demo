from __future__ import division
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.io.wavfile import write, read

def recordpulses(filename):

    '''
    record data from metronomes and save to .txt file
    '''

    # parameter
    duration = 8  # seconds
    ##sample_rate = 44100  # Hertz (CD quality)
    sample_rate = 22050  # Hertz (CD quality)
    
    # Record Audio
    print("start recording")
    
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float64')
    sd.wait()  # wait until recording is finished
    print("done recording")

    # Save to WAV file
    write('output.wav', sample_rate, audio_data)

    # save timeseries data to file
    times = np.linspace(0, duration, len(audio_data))
    Nt = len(times)
    
    ts = np.zeros([Nt,2])
    ts[:,0] = times
    ts[:,1] = audio_data[:,0]/np.max(np.abs(audio_data[:,0]))
    
    np.savetxt(filename, ts)
    
    # visualize the audio as a time-series
    DEBUG = 0
    if DEBUG:
        plt.plot(ts[:,0], ts[:,1], lw=2, color='b')
        plt.xlabel('time (sec)')
        plt.show()

    return
