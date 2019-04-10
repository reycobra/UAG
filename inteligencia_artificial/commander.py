#!/usr/bin/env python3

import speech_recognition as sr
import socket

SERVER = "127.0.0.1"
#SERVER = "192.168.43.138"
PORT = 65432

r = sr.Recognizer()
mic = sr.Microphone()
print("recording...")
with mic as source:
    audio = r.listen(source)

print("Analyzing...")
print(r.recognize_google(audio))

if __name__ == '__main__':

    pass
    # Connect to lego server
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     s.connect((SERVER, PORT))
    #     for movement in movements:
    #         print(movement)
    #         s.sendall(movement)
    #         data = s.recv(1024)
