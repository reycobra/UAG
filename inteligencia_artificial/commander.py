#!/usr/bin/env python3

import speech_recognition as sr
import socket

#SERVER = "127.0.0.1"
SERVER = "192.168.43.138"
PORT = 65432


if __name__ == '__main__':

    r = sr.Recognizer()
    mic = sr.Microphone()

    # Connect to lego server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER, PORT))
        while True:
            with mic as source:
                print("recording...")
                audio = r.listen(source, 10)
            try:
                print("Analyzing...")
                command = r.recognize_google(audio)
            except:
                command="wait"
            print(command)
            command = bytes(command, 'utf-8')
            s.sendall(command)
            data = s.recv(1024)
            if command == b'finish':
                break
            elif data == b'kill':
                break
