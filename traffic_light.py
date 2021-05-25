from gpiozero import LED # import gpiozero library
from time import sleep #import time library

# 17,5,12,27,6,16,22,13,20 GPIO outputs
#variable holds LED pin number

green = LED(17) 
green2 = LED(5)
green3 = LED(12)
yellow = LED(27)
yellow2 = LED(6)
yellow3 = LED(16)
red = LED(22)
red2 = LED(13)
red3 = LED(20)



try:
    
    while True:# the program will keep repeating itself indefinitely
        
        # turn on green light for valley 1
        green.off()
        green2.off()
        green3.on()
        yellow.off()
        yellow2.off()
        yellow3.off()
        red.on()
        red2.on()
        red3.off()
        sleep(5)
        
        #turn on warning sign
        green.off()
        green2.off()
        green3.off()
        yellow.on()
        yellow2.on()
        yellow3.on()
        red.off()
        red2.off()
        sleep(1)
        
        # turn on green light for north and southbound
        green.on()
        green2.on()
        green3.off() #turn off green light for valley 1
        yellow.off()
        yellow2.off()
        yellow3.off()
        red.off()
        red2.off()
        red3.on()
        sleep(5)
        
        #turn on warning sign
        green.off()
        green2.off()
        green3.off()
        yellow.on()
        yellow2.on()
        yellow3.on()
        red.off()
        red2.off()
        red3.off()
        sleep(1)

except KeyboardInterrupt: # press ctrl+c to end the program
    green.off()
    green2.off()
    green3.off()
    yellow.off()
    yellow2.off()
    yellow3.off()
    red.off()
    red2.off()
    red3.off()
