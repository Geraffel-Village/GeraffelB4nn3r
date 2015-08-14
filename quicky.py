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
    10,50,50,50,50,50,50,10,1000,20,
    10,50,50,50,80,80,50,10,1000,20,
    10,50,50,50,99,50,50,10,1000,20,
    10,50,50,50,50,99,50,10,1000,20,
    60,60,60,70,80,80,70,60,1000,20,
    60,60,60,99,80,80,60,60,1000,20,
    60,60,60,60,80,80,99,60,1000,20,
    60,60,70,80,80,80,80,70,1000,20,
    60,60,99,80,80,80,80,60,1000,20,
    60,60,60,80,80,80,80,99,1000,20,
    70,70,80,80,80,80,80,80,1000,20,
    99,60,80,80,80,80,80,80,1000,20,
    60,99,80,80,80,80,80,80,1000,20,
    80,80,80,80,80,80,80,80,1000,20,
    60,99,80,80,80,80,80,80,1000,20,
    99,60,80,80,80,80,80,80,1000,20,
    70,70,80,80,80,80,80,80,1000,20,
    60,60,60,80,80,80,80,99,1000,20,
    60,60,99,80,80,80,80,60,1000,20,
    60,60,70,80,80,80,80,70,1000,20,
    60,60,60,60,80,80,99,60,1000,20,
    60,60,60,99,80,80,60,60,1000,20,
    60,60,60,70,80,80,70,60,1000,20,
    50,50,50,50,50,99,50,50,1000,20,
    50,50,50,50,99,50,50,50,1000,20,
    50,50,50,50,80,80,50,50,1000,20,
    50,50,50,50,50,50,50,50,1000,20,
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
last=0
while x in range(len(ledpattern)):
    
    totaltime=(ledpattern[x+8])
    blendsteps=float(ledpattern[x+9])
    blendtime = totaltime/(1000*blendsteps)
    #print "_____________________________________________________________________"
    #print "Blendtime-total: ", totaltime, " Millisek.    ", "Blendtime-Steps: ", blendtime, " sek."
    if (x+10) == len(ledpattern):
        end=1
        last=len(ledpattern)
    step=0
    while step in range (int(blendsteps)):
        i=0
        while i in range(8): 
            difference =(ledpattern[x+i+10-last]-ledpattern[x+i])
            intervall = difference/blendsteps
            pwm= int(ledpattern[x+i] + intervall * (step+1))
            #print "Listenwert: ", ledpattern[x+i], "  Sollwert: ",ledpattern[x+i+10-last], "in ",int(blendsteps), " Schritten"
            #print "Differenz : ", difference, "  Steps: ", intervall,"  Cycle: ",pwm
            
            letters[i].ChangeDutyCycle(pwm)
                      
            i += 1
        
       
        sleep(blendtime)   #Pause entsprechend der softblendtime 
        
        step += 1
        #print "x=",x,"  Schritt=",step

    x +=10
    if end==1:
            break
 


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
