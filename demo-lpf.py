import numpy as np
from scipy.signal import butter, lfilter, freqz, filtfilt
import matplotlib.pyplot as plt
import scipy.signal as sigtool

my_data = np.genfromtxt('signal.csv', delimiter=',')

def rectifier(my_data):
    rect_data = (np.maximum(0, my_data))
    return rect_data

def butter_lowpass(cutoff, fs, order=5):
    return butter(order, cutoff, fs=fs, btype='low', analog=False)

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = filtfilt(b, a, data)
    return y

# Filter requirements.
order = 6
fs = 30.0
cutoff = 0.05
b, a = butter_lowpass(cutoff, fs, order)
T = 5.0
n = len(my_data) # total number of samples
t = np.linspace(0, T, n, endpoint=False)
data = rectifier(my_data)
y = butter_lowpass_filter(data, cutoff, fs, order)

def lowpass_filter():
    #plt.plot(t, y, 'g-', linewidth=2, label='filtered data')
    plt.xlabel('Time [sec]')
    plt.grid()
    plt.subplots_adjust(hspace=0.35)

def comparator():
    env = np.abs(sigtool.hilbert(my_data))
    treshold = np.max(env) / 9
    square_sig = ((y > treshold) * np.max(env))
    plt.plot(y, color='r', label='after LPF')
    plt.plot(square_sig, color='g', label='square')
    return square_sig

def main():
    print(rectifier(my_data))
    plt.plot(my_data, color='b', label='signal')
    #lowpass_filter()
    comparator()
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()