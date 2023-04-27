import numpy as np
from scipy.signal import butter, lfilter, freqz, filtfilt
from scipy.io import wavfile
import matplotlib.pyplot as plt
import scipy.signal as sigtool

plot = True
# Filter requirements.
order = 6
fs = 10.0
cutoff = 0.75
T = 5.0

def rectifier(my_data):
    rect_data = (np.abs(my_data))
    return rect_data

def butter_lowpass(cutoff, fs, order=5):
    return butter(order, cutoff, fs=fs, btype='low', analog=False)

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    print(len(data))
    y = filtfilt(b, a, data, padlen=len(data)-1)
    return y

def lowpass_filter():
    #plt.plot(t, y, 'g-', linewidth=2, label='filtered data')
    plt.xlabel('Time [sec]')
    plt.grid()
    plt.subplots_adjust(hspace=0.35)

def comparator(y, data):
    env = np.abs(data)
    treshold = np.max(env) * 0.2899
    square_sig = (y > treshold) * 1
    plt.plot(y, color='r', label='after LPF')
    plt.plot(square_sig * np.max(env), color='g', label='square')
    return square_sig

def main(data):
    n = len(data) # total number of samples
    data = rectifier(data)
    y = butter_lowpass_filter(data, cutoff, fs, order)
    #print(rectifier(data))
    plt.plot(data, color='b', label='signal')
    square_signal = comparator(y, data)
    plt.legend()
    if plot: 
        plt.show()
    
    np.savetxt("../demodulated_signal.csv", square_signal, delimiter=",")
    return square_signal

if __name__ == '__main__':
    sample_data = np.genfromtxt('../signal.csv', delimiter=',')
    #output_signal = main(sample_data)
    print(len(sample_data), sample_data)
    import wave
    import numpy as np

    with wave.open("../recorded_signals_urh/1_off/out2.wav") as f:
        # Read the whole file into a buffer. If you are dealing with a large file
        # then you should read it in blocks and process them separately.
        buffer = f.readframes(f.getnframes())
        # Convert the buffer to a numpy array by checking the size of the sample
        # with in bytes. The output will be a 1D array with interleaved channels.
        interleaved = np.frombuffer(buffer, dtype=f'int{f.getsampwidth()*8}')
        # Reshape it into a 2D array separating the channels in columns.
        data = np.reshape(interleaved, (-1, f.getnchannels()))

    #data = data/max(data)
    data = np.hstack(data)
    print(len(data), data)
    output_signal = main(data)
    np.savetxt("../demodulated_signal.csv", output_signal, delimiter=",")
    print(output_signal)