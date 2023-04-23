from record import record
from gpiozero import Button
from time import sleep
from gpiozero import RGBLED

if __name__ == "__main__":
    button = Button("GPIO4")

    led = RGBLED(red="GPIO22", green="GPIO23", blue="GPIO27")
    while True:
        led.color = (1, 0.5, 1)

        if button.is_pressed:
            led.color = (1, 0, 0)
            record()
            led.color = (0, 1, 0)
            sleep(5)

