#!/bin/sh
#
# led.sh
#######################################################################
# This outputs a pattern on gpio under wiringpi
# https://projects.drogon.net/raspberry-pi/wiringpi/
#######################################################################


# Variablen entsprechen den Buchstaben des Geraffel-Banners und 
# verweisen auf den jeweiligen GPIO-Port

G=15
E1=16
R=1
A=4
F1=5
F2=6
E2=10
L=11


#gpio mode $G pwm
#gpio mode $E1 pwm

gpio mode $R pwm
gpio mode $A pwm

#gpio mode $F1 pwm
#gpio mode $F2 pwm
#gpio mode $E2 pwm
#gpio mode $L pwm

# Erst mal alles löschen
#gpio write $G 0
#gpio write $E1 0
#gpio write $R 0
#gpio write $A 0
#gpio write $F1 0
#gpio write $F2 0
#gpio write $E 0
#gpio write $L 0

i=1
#while [ $i -le 5 ]  
#do

  i=$(($i+1))

  #gpio pwm $G 1000
  #gpio pwm $E1 200
  gpio pwm $R 300
  gpio pwm $A 800
  #gpio pwm $F1 500
  #gpio pwm $F2 600
  #gpio pwm $E 700
  #gpio pwm $L 800
  sleep 3.0

#done
