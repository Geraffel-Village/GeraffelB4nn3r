 #!/usr/bin/python
#
# pwm-test
#######################################################################
# This outputs a pattern on gpio under wiringpi
# https://projects.drogon.net/raspberry-pi/wiringpi/
#######################################################################


# Variablen entsprechen den Buchstaben des Geraffel-Banners und 
# verweisen auf den jeweiligen GPIO-Port



#LEDMUSTER:
ledpattern = [
    1,99, 1,99, 1,99, 1,99,  3000, 20,
    99, 1,99, 1,99, 1,99, 1,  3000, 20,
     1,99, 1,99, 1,99, 1,99,  3000, 20,
    99, 1,99, 1,99, 1,99, 1,  3000, 20,
    99, 1,99, 1,99, 1,99, 1,  1000, 20,
    50,50,50,50,50,50,50,50,  3000, 20,
    50,50,50,50,50,50,50,50,  2000, 1,
     1, 1, 0, 0, 0, 0, 1, 1,  3000, 8,
     1, 1, 0, 0, 0, 0, 1, 1,  2000, 20,
     1, 2, 4, 8,16,32,64,99,  3000, 30,
     1, 2, 4, 8,16,32,64,99,  1000, 1,
    99,64,32,16, 8, 4, 2, 1,  3000, 30,
    99,64,32,16, 8, 4, 2, 1,  1000, 20,
    99,99,99,99,99,99,99,99,  3000, 40,
    99,99,99,99,99,99,99,99,  2000, 40, 
     ]
    
#_____________________________________________________________________
#Pinbelegung laut RPi-Board entsprechend zu den Buchstaben des Banners
G=14
E1=15
R=18
A=23
F1=24
F2=25
E2=8
L=7

gpios =    [14, 15, 18, 23, 24, 25, 8, 7]
letters = ["G", "E1", "R", "A", "F1", "f2", "E2", "L"]
frequenz=100    #PWM-Frequenz in Hz
end=0

import RPi.GPIO as GPIO
from time import sleep
from random import randint

#set up gpio
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

i=0
while i in range(8):
    gpio = gpios[i]                         #aktuelen GPIO aus Liste nehmen
    GPIO.setup(gpio,GPIO.OUT)               #und auf Ausgang stellen
    letters[i] = GPIO.PWM(gpio,frequenz)    #Buchstabe aus 1.Liste holen und als PWM schalten mit    
    letters[i].start(ledpattern[i])          #akt. Buchstaben mit akt. PWM Wert starten        
    i += 1

x=0
while x in range(50):

    i=0
    while i in range(8):
        pwm=randint(0,99)
        letters[i].ChangeDutyCycle(pwm)
        i += 1
    
    
    time=(randint(200,3000))   #Pause im millisekunden
    sleep(time/1000)            #Pause in sekunden
    x += 1

#Cleanup
        
#PWM.stop()
GPIO.cleanup()
#G.stop()
#E1.stop()
#R.stop()
#A.stop()
#F1.stop()
#F2.stop()
#E2.stop()
#L.stop()
