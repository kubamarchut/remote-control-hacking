from sample import main as sampleMain
from decode import main as decodeMain
from demodulate import main as demodulateMain
from record import record
from gpiozero import Button
from gpiozero import RGBLED
from time import sleep

if __name__ == "__main__":
    button = Button("GPIO4")

    led = RGBLED(red="GPIO22", green="GPIO23", blue="GPIO27")
    while True:
        led.color = (1, 0.5, 1)

        if button.is_pressed:
            led.color = (1, 0, 0)
            print("recording signal")
            recorded_data = record()

            led.color = (0, 1, 1)
            print("demodulating data")
            demodulated_data = demodulateMain(recorded_data)

            led.color = (0, 0, 1)
            print("sampling signal")
            sampled_data = sampleMain(demodulated_data)

            led.color = (1, 0, 1)
            print("decoding data")
            decoded_code = decodeMain(sampled_data)

            led.blink(1, 1, 1, 1, (0, 1, 0), (0, 0, 0), 5)
            print("output:", decoded_code)


