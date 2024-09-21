#  Source code from the echo-client example from the gitHub repo. rpc-client has hardcoded requests, that it can send as messages to 
# the server and get a response back. Handles typical errors when creating a socket and connecting to the server, and can send multiple
# messages and receive responses to each one. 

import socket

HOST = "127.0.0.1"  
PORT = 65432  
REQ1 = "List the best dining halls at Smith"
REQ2 = "What is the best Haynes Stir Fry sauce"
REQ3 = "What are the dinner hours"


print("client starting - connecting to dining server at IP", HOST, "and port", PORT,"\n")

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print(f"could not create socket\n")

try:
    s.connect((HOST, PORT))
except socket.gaierror:
    print("connection error.")

# sendMessage takes in a String message, encodes it, and sends it to the server. Also handles the response and updates with progress messages
def sendMessage(message):
    # print(f"> ")
    # message = input()
    print(f"connection established, sending request '{message}'\n")
    s.sendall(bytes(message, 'utf-8'))
    print("message sent, waiting for reply\n")
    data = s.recv(1024)
    print(f"meceived response: '{data!r}' [{len(data)} bytes]\n")
    print("client is done!\n")  
    
sendMessage(REQ1)
sendMessage(REQ2)
sendMessage(REQ3)
