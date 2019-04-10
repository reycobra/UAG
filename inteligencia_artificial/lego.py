#!/usr/bin/env python3

# This program is intended to provided a set of functions to move a lego mindstorm
# ev3 using the debian based distro ev3dev and was made for a Mexican school project
# at Universidad Autonoma de Guadalajara
#
# ev3dev info on: https://www.ev3dev.org/
# school info on: http://www.uag.mx/
#
# The lego functions are implemented thinking on the lego as a tank vehicule with
# a gripper in the front and two sensors of his back
#

# Packages
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
import socket

HOST = "127.0.0.1"                                                              # LEGO IP address
PORT = 65432                                                                    # Port to listen on (non-privileged ports are > 1023)

# Classes
class lego_tank():

    def __init__(self):

        #try:
        #    self.tank_drive = MoveTank(OUTPUT_D, OUTPUT_A)
        #    self.print("Create the tank_drive")
        #except:
        #    self.tank_drive = False

        #self.degrees = 5
        sound = Sound()
        self.tank_drive = MoveTank(OUTPUT_D, OUTPUT_A)
        print("Create the tank_drive")

        self.degrees = 1230

    def right(self):
        if self.tank_drive:
            print("I am moving to right")
            self.tank_drive.on_for_degrees(50 , -50, 470)
        else:
            # We do not have outputs if we run this from our own computer
            pass

    def left(self):
        if self.tank_drive:
            print("I am moving to left")
            self.tank_drive.on_for_degrees(-50 , 50, 470)
        else:
            # We do not have outputs if we run this from our own computer
            pass

    def forward(self):
        if self.tank_drive:
            print("I am moving forward")
            self.tank_drive.on_for_degrees(50 , 50, self.degrees)
        else:
            # We do not have outputs if we run this from our own computer
            pass

    def backward(self):
        if self.tank_drive:
            print("I am moving backwards")
            self.tank_drive.on_for_degrees(50 , 50, (-1) * self.degrees)
        else:
            # We do not have outputs if we run this from our own computer
            pass


# Demo code
if "__main__"==__name__:
    lego = lego_tank()
    lego.right()
    lego.right()
    lego.right()
    lego.right()
