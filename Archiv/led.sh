!/bin/sh
#
# led.sh
#######################################################################
# This outputs a pattern on gpio under wiringpi
# https://projects.drogon.net/raspberry-pi/wiringpi/
#
#  4 
#######################################################################

# LED Pin - wiringPi pin 0 is BCM_GPIO 17.

#PIN=0

G=15
E1=16
R=1
A=4
F1=5
F2=6
E2=10
L=11

echo "Testausgabe zur Kontrolle"

gpio mode $G out
gpio mode $E1 out
gpio mode $R out
gpio mode $A out
gpio mode $F1 out
gpio mode $F2 out
gpio mode $E2 out
gpio mode $L out

gpio write $G 0
gpio write $E1 0
gpio write $R 0
gpio write $A 0
gpio write $F1 0
gpio write $F2 0
gpio write $E 0
gpio write $L 0

#while true; do
  gpio write $G 1
  sleep 0.5
  gpio write $E1 1
  sleep 0.5
  gpio write $R 1
  sleep 0.5
  gpio write $A 1
  sleep 0.5
  gpio write $F1 1
  sleep 0.5
  gpio write $F2 1
  sleep 0.5
  gpio write $E2 1
  sleep 0.5
  gpio write $L 1
  sleep 1.5

  gpio write $G 0
  sleep 0.5
  gpio write $E1 0
  sleep 0.5
  gpio write $R 0
  sleep 0.5
  gpio write $A 0
  sleep 0.5
  gpio write $F1 0
  sleep 0.5
  gpio write $F2 0
  sleep 0.5
  gpio write $E2 0
  sleep 0.5
  gpio write $L 0
  sleep 1.5
#done
