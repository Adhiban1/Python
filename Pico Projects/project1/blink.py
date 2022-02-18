# This program blinks the Builtin LED of Raspberry pi pico

from machine import Pin
import time

pin = Pin(25, Pin.OUT)

while True:
    pin.toggle()
    time.sleep_ms(1000) # one second
