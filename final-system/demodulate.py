import numpy as np
from scipy.signal import butter, lfilter, freqz, filtfilt
import scipy.signal as sigtool

plot = True
# Filter requirements.
order = 6
fs = 10
cutoff = 0.75
T = 5.0


def rectifier(my_data):
    rect_data = (np.abs(my_data))
    return rect_data


def butter_lowpass(cutoff, fs, order=5):
    return butter(order, cutoff, fs=fs, btype='low', analog=False)


def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = filtfilt(b, a, data)
    return y


def comparator(y, data):
    env = np.abs(data)
    treshold = np.max(env) * 0.2899
    square_sig = (y > treshold) * 1
    return square_sig


def main(data):
    n = len(data)  # total number of samples
    b, a = butter_lowpass(cutoff, fs, order)
    data = rectifier(data)
    t = np.linspace(0, T, n, endpoint=False)
    y = butter_lowpass_filter(data, cutoff, fs, order)
    # print(rectifier(data))

    square_signal = comparator(y, data)

    np.savetxt("../demodulated_signal.csv", square_signal, delimiter=",")
    return square_signal


if __name__ == '__main__':
    sample_data = np.genfromtxt('../signal.csv', delimiter=',')
    output_signal = main(sample_data)
    np.savetxt("../demodulated_signal.csv", output_signal, delimiter=",")
    print(output_signal)
