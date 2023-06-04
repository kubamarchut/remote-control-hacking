from sample import main as sampleMain
from decode import decode as decodeMain
from demodulate import main as demodulateMain
#from send import sendMain
from record import record
from record import decimate
from gpiozero import Button
from gpiozero import RGBLED
from time import sleep
from record import current_time


TRANSMIT_PIN = 37
sequence1_off = '0001010001010101001111000'
if __name__ == "__main__":
    button = Button("GPIO4")
    button2 = Button("GPIO2")
    led = RGBLED(red="GPIO22", green="GPIO23", blue="GPIO27")
    while True:
        try:
            led.color = (1, 0.5, 1)

            if button2.is_pressed:
                # sendMain(sequence1_off)
                #led.color = (1, 0, 0)
                print("")

            if button.is_pressed:
                led.color = (1, 0, 0)
                print("timestamp:",  str(current_time()),
                      "signal recording - start")
                recorded_data = record()
                print("timestamp:",  str(current_time()),
                      "signal recording - end")

                led.color = (1, 1, 0)
                print("timestamp:",  str(current_time()), "decimating signal")
                decimated_data = decimate(recorded_data)

                led.color = (0, 1, 1)
                print("timestamp:", str(current_time()), "demodulating data")
                demodulated_data = demodulateMain(decimated_data)

                led.color = (0, 0, 1)
                print("timestamp:", str(current_time()), "sampling signal")
                sampled_data = sampleMain(demodulated_data)

                if sampled_data:
                    led.color = (1, 0, 1)
                    print("timestamp:", str(current_time()), "decoding data")
                    decoded_code = decodeMain(sampled_data[0])

                    if decoded_code != False:
                        led.blink(1, 1, 1, 1, (0, 1, 0), (0, 0, 0), 5)
                        print("timestamp:", str(current_time()),
                              "output:", decoded_code)
                    else:
                        print("timestamp:", str(current_time()),
                              "nie znaleziono kodu pilota")
                else:
                    print("timestamp:", str(current_time()),
                          "nie znaleziono kodu pilota")
        except KeyboardInterrupt:
            print("The Program is terminated manually")
            raise SystemExit
