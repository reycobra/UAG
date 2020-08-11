# Distributed systems

In this folder you can find 2 practices developed for the class of distributed
systems.

## Indirect Communication - Publish and subscribe

### Goals

The goal of this practice is to made a simple application capable of show the
use of the indirect communication through the MQTT protocol

### Requirements

- Python 3
- packages from the requirements.txt file
- mosquitto program
- paho-mqtt package

### Usage

Follow the next steps to use this project
- Run the broker
- Run the subscriber
- Run the publisher with the message you want

### Authors

LEGO team UAG

## Sockets - Peer to Peer communication between a client and a server

### Goals

The goal of this practice is to make a simple application that can show how
two nodes can communicate between them.
We choose to present the example with a client and server nodes.

### Requirements

- python 3
- click package
- fire package

### Usage

For been able to use this project first you need to follow the next steps
- Run the server in a terminal
- Run the client in another terminal and add the desire message to send to the
  server
- Observe how the server receive the message and answers
- The server can be stopped by sending from the client the message 'stop'

### Authors

Team LEGO UAG
