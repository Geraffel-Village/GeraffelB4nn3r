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

import RPi.GPIO as GPIO
from time import sleep

#set up gpio

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(G,GPIO.OUT)
GPIO.setup(E1,GPIO.OUT)
GPIO.setup(R,GPIO.OUT)
GPIO.setup(A,GPIO.OUT)
GPIO.setup(F1,GPIO.OUT)
GPIO.setup(F2,GPIO.OUT)
GPIO.setup(E2,GPIO.OUT)
GPIO.setup(L,GPIO.OUT)

frequenz=100     #PWM-Frequenz in Hz

G  = GPIO.PWM(G,frequenz)
E1 = GPIO.PWM(E1,frequenz)
R  = GPIO.PWM(R,frequenz)
A  = GPIO.PWM(A,frequenz)
F1 = GPIO.PWM(F1,frequenz)
F2 = GPIO.PWM(F2,frequenz)
E2 = GPIO.PWM(E2,frequenz)
L  = GPIO.PWM(L,frequenz)

G.start(100)
E1.start(80)
R.start(65)
A.start(50)
F1.start(40)
F2.start(30)
E2.start(15)
L.start(2)


sleep(5.1)
G.ChangeDutyCycle(10)
sleep(3.1)
L.ChangeDutyCycle(2)
R.ChangeDutyCycle(65)
sleep(1)
E1.ChangeDutyCycle(2)
R.ChangeDutyCycle(65)
sleep(1)
L.ChangeDutyCycle(2)
R.ChangeDutyCycle(65)
sleep(1)
L.ChangeDutyCycle(2)
R.ChangeDutyCycle(65)
sleep(1)

#Cleanup
PWM.stop()
GPIO.cleanup()
G.stop()
E1.stop()
R.stop()
A.stop()
F1.stop()
F2.stop()
E2.stop()
L.stop()
