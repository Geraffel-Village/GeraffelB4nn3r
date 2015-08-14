#!/usr/bin/python
#
# pwm-test
#######################################################################
# This outputs a pattern on gpio under wiringpi
# https://projects.drogon.net/raspberry-pi/wiringpi/
#######################################################################


# Variablen entsprechen den Buchstaben des Geraffel-Banners und 
# verweisen auf den jeweiligen GPIO-Port

#Pinbelegung laut RPi-Board
G=14
E1=15
R=18
A=23
F1=24
F2=25
E2=8
L=7

ledvalues = [2, 5, 10, 16, 30, 50, 75, 100,]
idlevalues = [ 2, 2, 2, 55, 55, 2, 2, 2]
gpios =    [14, 15, 18, 23, 24, 25, 8, 7]
letters = ["G", "E1", "R", "A", "F1", "f2", "E2", "L"]
frequenz=100     #PWM-Frequenz in Hz

#LEDMUSTER:
ledpattern2 = [
    1,10,45,99,99,45,10,1,  1,
    99,45,10,1,1,10,45,99,  1,
    1,10,45,99,99,45,10,1,  1,
    99,45,10,1,1,10,45,99,  1,
    1,10,45,99,99,45,10,1,  1,
    99,45,10,1,1,10,45,99,  1,
    1,10,45,99,99,45,10,1,  1,
    99,45,10,1,1,10,45,99,  1,
    2,55,4,99,6,
    ]
    
ledpattern = [
     1, 2, 2,99,99, 2, 2, 1,   2000, 
     2, 4, 6,95,95, 6, 4, 2,   500,
     4, 7,10,90,90,10, 7, 4,   500,
     6,10,15,85,85,15,10, 6,   500,
     9,14,20,78,78,20,14, 9,   500,
    12,18,25,71,71,25,18,12,   500,
    16,23,30,64,64,30,23,16,   500,
    20,28,35,57,57,35,28,20,   500,
    24,33,40,50,50,40,33,24,   500,
    29,38,46,44,44,46,38,29,   500,
    34,43,52,39,39,52,43,34,   500,
    39,49,59,34,34,59,49,39,   500,
    44,54,66,30,30,66,54,44,   500,
    49,60,73,26,26,73,60,49,   500,
    54,66,80,22,22,80,66,54,   500,
    60,73,87,18,18,87,73,60,   500,
    66,80,94,12,12,94,80,66,   500,
    72,87,99, 8, 8,99,87,72,   500,
    78,99,90, 6, 6,90,99,78,   500,
    85,80,70, 4, 4,70,80,85,   500,
    92,65,40, 2, 2,40,65,92,   500,
    99,50,25, 2, 2,25,50,99,   500,
    99,30,10, 1, 1,10,30,99,   5000,
    ]
    


import RPi.GPIO as GPIO
from time import sleep

#set up gpio

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

i=0
while i in range(8):
    gpio = gpios[i]                         #aktuelen GPIO aus Liste nehmen
    GPIO.setup(gpio,GPIO.OUT)               #und auf Ausgang stellen
    letters[i] = GPIO.PWM(gpio,frequenz)    #Buchstabe aus 1.Liste holen und als PWM schalten mit    
    letters[i].start(ledvalues[i])          #akt. Buchstaben mit akt. PWM Wert starten        
    sleep(0.2)
    i += 1


x=0
while x in range(len(ledpattern)):
    i=0 
    while i in range(8): 
        letters[i].ChangeDutyCycle(ledpattern[x])
        print i
        i += 1
        print x
        x += 1
    sleep(ledpattern[x/1000])
    x += 1

          


#Cleanup
#PWM.stop()
#GPIO.cleanup()
#G.stop()
#E1.stop()
#R.stop()
#A.stop()
#F1.stop()
#F2.stop()
#E2.stop()
#L.stop()
