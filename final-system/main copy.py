from sample import main as sampleMain
from decode import decode as decodeMain
from demodulate import main as demodulateMain
from record import record
from time import sleep

if __name__ == "__main__":
    print("recording signal")
    recorded_data = record()

    print("demodulating data")
    demodulated_data = demodulateMain(recorded_data)

    print("sampling signal")
    sampled_data = sampleMain(demodulated_data)

    print("decoding data")
    decoded_code = decodeMain(sampled_data)

    print("output:", decoded_code)


