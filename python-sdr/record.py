from scipy import signal
import numpy as np
from rtlsdr import RtlSdr
from scipy.io import wavfile
from rtlsdr import *
N = 8192000
FREQ = 433.92e6
F_OFFSET = 0.02e6
GAIN = 15
SAMPLE_RATE = 1e6


def record():
    fc = FREQ - F_OFFSET
    sdr = RtlSdr()
    sdr.center_freq = fc
    sdr.sample_rate = SAMPLE_RATE
    sdr.gain = GAIN
    samples = sdr.read_samples(N)
    decimated = signal.decimate(samples, 20) #Dla wartości 20 jest jeszcze w miarę ładnie widoczny sygnał
    scaled = np.int16(decimated / np.max(np.abs(decimated)) * 32767)
    wavfile.write('../../remote-control-hacking/recorded_signals_urh/1_off/out.wav', int(sdr.sample_rate), scaled.astype("int16"))
    return scaled


if __name__ == "__main__":
    record()

