# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Ustawienie pinu do kontroli nadajnika FS1000A
transmit_pin = 37
GPIO.setup(transmit_pin, GPIO.OUT)

# Sekwencja bitow do wys³ania 1332675
sequence2_on ='0001010001010101110000110' #gniazdko 2 w³¹czenie
sequence1_on ='0001010001010101001100110' #gniazdko 1  
sequence1_off = '0001010001010101001111000'
# Ustawienie parametrów czasowych
zero_delay = 0.00016*0.66  # Dlugosc czasu trwania bitu 0
one_delay = 0.0005*0.66   # Dlugosc czasu trwania bitu 1
gap_zero = 0.00054*0.66  # Dlugosc czasu przerwy miêdzy bitami
gap_one = 0.0002*0.66
gap_signal = 0.0053*0.66


def send_bit(bit):
    if bit == '0':
        GPIO.output(transmit_pin, GPIO.HIGH)
        time.sleep(zero_delay)
        GPIO.output(transmit_pin, GPIO.LOW)
        time.sleep(gap_zero)
        
    elif bit == '1':
        GPIO.output(transmit_pin, GPIO.HIGH)
        time.sleep(one_delay)
        GPIO.output(transmit_pin, GPIO.LOW)
        time.sleep(gap_one)
        
def sendMain(sequence):
  i=0
  while i<15:
    for bit in sequence:
      send_bit(bit)
    time.sleep(gap_signal)
    i+=1
  GPIO.cleanup()
    
if __name__ == "__main__":
# Wysylanie sekwencji bitow
  i=0
  while i<15:
    for bit in sequence1_off:
      send_bit(bit)
    time.sleep(gap_signal)
    i+=1
  GPIO.cleanup()