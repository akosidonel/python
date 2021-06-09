#Simple park sensor using Raspberry pi and HC-SR04 Ultrasonic sensor

from gpiozero import DistanceSensor, LED
from time import sleep

green = LED(17)
red = LED(22)



ultrasonic = DistanceSensor(echo=23,trigger=4)

try:
    while True:
        ultrasonic.wait_for_in_range()
        print('Occupied')
        green.off()
        red.on()
        ultrasonic.wait_for_out_of_range()
        print('Vacant')
        green.on()
        red.off()
        
except KeyboardInterrupt:
    green.off()
    red.off()
    print('Device is turn off...Goodbye')
