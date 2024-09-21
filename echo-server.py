#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

print("server starting - listening for connections at IP", HOST, "and port", PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept() #connection to send and recive data 
    with conn: #can ignore, pretend not there. important though, with connection
        print(f"Connected established with {addr}") #telling user whats up
        while True:
            data = conn.recv(1024) #every time this runs, object with method recv, takes in 1024 num. bytes. 
            if not data: #if empty string, not data equates to false, break out of while loop 
                break
            print(f"Received client message: '{data!r}' [{len(data)} bytes]")
            print(f"echoing '{data!r}' back to client")
            conn.sendall(data) #instead of sending data, you coulf send back string "im not home"

print("server is done!")
