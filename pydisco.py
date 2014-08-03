# pydisco.py
#
# Based on the tutorial from micropython.org

# Import the pyboard library
import pyb


LED_PIN_MIN = 1
LED_PIN_MAX = 5

# Assignment of physical LEDs to the leds array
leds = [pyb.LED(index) for index in range(LED_PIN_MIN,LED_PIN_MAX)]

# Turn off all leds for starting state
for activeLed in leds: 
    activeLed.off()

# Disco LEDs
num = 0
try:
   while True:
      num = (num + 1) % 4
      leds[num].toggle()
      pyb.delay(50)
finally:
    for activeLed in leds:
        activeLed.off()