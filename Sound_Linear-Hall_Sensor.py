import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

sound_pin = 17
hall_pin = 27

gpio.setup(sound_pin, gpio.IN)
gpio.setup(hall_pin, gpio.IN)

try:
    while True:
        sound_value = gpio.input(sound_pin)
        hall_value = gpio.input(hall_pin)
        
        print("Sound Sensor: ", sound_value)
        print("Hall Sensor: ", hall_value)

        
except KeyboardInterrupt:
    gpio.cleanup()