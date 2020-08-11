# Artificial Intelligence

## Description

This directory have all the material done for my Artificial Intelligence
class, there are two projects here, one related with resolving a maze using
lego mindstorm and another one related to control the lego mindstorm with
voice commands.

### Brief description of the "Maze project"

The main idea here is edit a fixed graph representing all the paths of the
maze inside the script maze.py, after that you just need to put the lego.py
sctip and the maze.py script inside the lego mindstorm and that will be all.

### Brief description of the "Lego speech recognition commands project"

This projects enables to speak to the laptop and the lego do the commands.
Here you just need to put the lego.py code in the lego mindstorm, and then run
both of the scripts and start speaking commands to the lego mindstorm with
your laptop microphone.

The voice commands implemented were:
  - run
  - forward
  - backward
  - left
  - right

## Tools

- 1 Lego ev3 mindstorm
- 1 usb-wifi nano card
- 1 laptop powered by GNU/Linux
- 1 MicroSD card

## Software

- ev3dev operating system
- Python packages, python version 3.6.0:
  - evdev
  - python-ev3dev2
  - speechrecognition
  - pyaudio
  - pipenv

**Important Notice:** *Pipenv was showing a dependency tree error due to pyaudio, I didn't have the properly time to debug that, my apologies for issues casued by this*

