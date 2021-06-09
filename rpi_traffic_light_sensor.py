from gpiozero import DistanceSensor, TrafficLights # gpiozero libraries
from time import sleep
from signal import pause

# define the red,amber,green LED pin as output
traffic_light1 = TrafficLights(22,27,17) # north bound traffic light
traffic_light2 = TrafficLights(13,6,5) # south bound traffic light
traffic_light3 = TrafficLights(20,16,12) # valley 1 traffic light

#set up HC-SR04 echo and trigger pin as input
sensor = DistanceSensor(23,4,max_distance=2) 

#signal light function for sensor detection
# stop signal for north/south bound
# go signal for valley 1
def signal_light2():
    traffic_light1.red.on()
    traffic_light1.amber.off()
    traffic_light1.green.off()
    traffic_light2.red.on()
    traffic_light2.amber.off()
    traffic_light2.green.off()
    traffic_light3.red.off()
    traffic_light3.amber.off()
    traffic_light3.green.on() 
    sleep(2)

try:    
    while True:
        Distance = sensor.distance * 100 # measuring the distance and convert it into cm
        sleep(1) # sensor sleep for 1 seconds
        if Distance < 100: # if the value of distance is less than 100
            signal_light2() # activate the function for valley 1 signal light
            print('Distance sensor read ', Distance, ' cm. red,red, green') 
        else: # if the distance value is greater than 100 it will run the default timer for 3 signal light
            print('Distance sensor read ',Distance,' cm. Default timer')
            while True:
                traffic_light1.red.on() # stop signal for north bound traffic
                traffic_light1.amber.off()
                traffic_light1.green.off()
                traffic_light2.red.on() # stop signal for south bound traffic
                traffic_light2.amber.off()
                traffic_light2.green.off()
                traffic_light3.red.off() # go signal for valley 1 traffic
                traffic_light3.amber.off()
                traffic_light3.green.on() 
                sleep(2) # standby for 2 seconds until the cycle begins
                
                traffic_light1.red.off() # all warning LED light is on
                traffic_light1.amber.on()
                traffic_light1.green.off()
                traffic_light2.red.off()
                traffic_light2.amber.on()
                traffic_light2.green.off()
                traffic_light3.red.off()
                traffic_light3.amber.on()
                traffic_light3.green.off() 
                sleep(1) # standby for 1 sec
                
                traffic_light1.red.off()# go signal for north bound traffic
                traffic_light1.amber.off()
                traffic_light1.green.on()
                traffic_light2.red.off()# go signal for south bound traffic
                traffic_light2.amber.off()
                traffic_light2.green.on()
                traffic_light3.red.on() # stop signal for valley 1 traffic
                traffic_light3.amber.off()
                traffic_light3.green.off() 
                sleep(2) #standby for 2 seconds until the cycle begins
                
                traffic_light1.red.off() #all warning LED light is on
                traffic_light1.amber.on()
                traffic_light1.green.off()
                traffic_light2.red.off()
                traffic_light2.amber.on()
                traffic_light2.green.off()
                traffic_light3.red.off()
                traffic_light3.amber.on()
                traffic_light3.green.off() 
                sleep(1)# standby for 1 sec
                
                 break #if the distance value is less than 100cm .. then break the loop
               
    pause()     
except KeyboardInterrupt: #ctrl C to turn off the LED and sensor
    traffic_light1.off()
    traffic_light2.off()
    traffic_light3.off()
    print('Device off......')
    
 
