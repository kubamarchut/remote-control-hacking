from scipy import signal

from numpy import max, abs, int16


from rtlsdr import RtlSdr
from scipy.io import wavfile

N = 4096000
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
    scaled = int16(decimated / max(abs(decimated)) * 32767)
    wavfile.write('../../remote-control-hacking/recorded_signals_urh/1_off/out2.wav', int(sdr.sample_rate), scaled.astype("int16"))
    return scaled


if __name__ == "__main__":
    record()

