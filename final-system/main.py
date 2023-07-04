import time, os
from gpio_handler import *
from sample import main as sampleMain
from decode import decode as decodeMain
from demodulate import main as demodulateMain
from send import sendMain
from record import record, initialize
from record import decimate
from time import sleep

ispulsing = False
sequence = '0001010001010101001111000'
initialize()
os.system('clear')
if __name__ == "__main__":
    print("program ready")
    while True:
        try:
            led(1, 1, 1)
            if not GPIO.input(BUTTON_2_PIN):
                led(0, 1, 0)
                print("timestamp:",  str(current_time()), "sending code:",  sequence)
                sendMain(sequence)

            if not GPIO.input(BUTTON_1_PIN):
                led(1, 0, 0)
                print("timestamp:",  str(current_time()),
                      "signal recording - start")
                recorded_data = record()
                print("timestamp:",  str(current_time()),
                      "signal recording - end")

                led(1, 1, 0)
                print("timestamp:",  str(current_time()), "decimating signal")
                decimated_data = decimate(recorded_data)

                led(0, 1, 1)
                print("timestamp:", str(current_time()), "demodulating data")
                demodulated_data = demodulateMain(decimated_data)

                led(0, 0, 1)
                print("timestamp:", str(current_time()), "sampling signal")
                sampled_data = sampleMain(demodulated_data)

                if sampled_data:
                    led(1, 0, 1)
                    print("timestamp:", str(current_time()), "decoding data")
                    decoded_code = decodeMain(sampled_data[0])

                    if decoded_code != False:
                        led(1,1,1)
                        sequence = decoded_code[0] + "0"
                        print("timestamp:", str(current_time()),
                              "output:", decoded_code)
                    else:
                        print("timestamp:", str(current_time()),
                              "nie znaleziono kodu pilota")
                else:
                    print("timestamp:", str(current_time()),
                          "nie znaleziono kodu pilota")

        except KeyboardInterrupt:
            led(0,0,0)
            print("The Program is terminated manually")
            raise SystemExit
