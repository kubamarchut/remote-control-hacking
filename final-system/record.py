from scipy import signal
from numpy import max, abs, int16
from rtlsdr import RtlSdr
from scipy.io import wavfile
from datetime import datetime

N = 4096000
FREQ = 433.92e6
F_OFFSET = 0.02e6
GAIN = 15
SAMPLE_RATE = 1e6


def current_time():
    time = datetime.now()
    current_time = time.strftime("%H:%M:%S")
    return current_time


def record():
    # print("start")
    fc = FREQ - F_OFFSET
    sdr = RtlSdr()
    sdr.center_freq = fc
    sdr.sample_rate = SAMPLE_RATE
    sdr.gain = GAIN
    samples = sdr.read_samples(N)
   # decimated = signal.decimate(samples, 20) #Dla wartości 20 jest jeszcze w miarę ładnie widoczny sygnał
   # scaled = int16(decimated.real / max(abs(decimated)) * 32767)
   # wavfile.write('../../remote-control-hacking/recorded_signals_urh/1_off/out2.wav', int(sdr.sample_rate), scaled.astype("int16"))
    # print("end")
    return samples


def decimate(samples):
    # Dla wartości 20 jest jeszcze w miarę ładnie widoczny sygnał
    decimated = signal.decimate(samples, 20)
    scaled = int16(decimated.real / max(abs(decimated)) * 32767)
    return scaled
