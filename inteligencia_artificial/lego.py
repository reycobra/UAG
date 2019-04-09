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
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
import socket

HOST = "127.0.0.1"                                                              # LEGO IP address
PORT = 65432                                                                    # Port to listen on (non-privileged ports are > 1023)

# Classes
class lego_tank():

    def __init__(self):
        try:
            self.tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
        except:
            self.tank_drive = False

        self.rotations = 5

    def right(self):
        print("I'm moving to right")
        if self.tank_drive:
            self.tank_drive.on_for_rotations(5 , 1, self.rotations)
            self.tank_drive.on_for_rotations(5 , 5, self.rotations)
        else:
            # We do not have outputs if we run this from our own computer
            pass

    def left(self):
        print("I'm moving to left")
        if self.tank_drive:
            self.tank_drive.on_for_rotations(1 , 5, self.rotations)
            self.tank_drive.on_for_rotations(5 , 5, self.rotations)
        else:
            # We do not have outputs if we run this from our own computer
            pass

    def forward(self):
        print("I'm moving forward")
        if self.tank_drive:
            self.tank_drive.on_for_rotations(5 , 5, self.rotations)
        else:
            # We do not have outputs if we run this from our own computer
            pass

    def backward(self):
        print("I'm moving backwards")
        if self.tank_drive:
            self.tank_drive.on_for_rotations(5 , 5, (-1) * self.rotations)
        else:
            # We do not have outputs if we run this from our own computer
            pass


# Demo code
if "__main__"==__name__:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        lego = lego_tank()
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                elif data == "left":
                    lego.left()
                elif data == "right":
                    lego.right()
                elif data == "forward":
                    lego.forward()
                elif data == "backward":
                    lego.backward()
                conn.sendall(b"done")
