# Source code from the echo-server example from the gitHub repo. Creates a socket from the localhost and given port, and recives specific 
# client messages and responds to them. Decodes the data, matches the question with the response, encodes the response, and sends it back 
# to the client. Can answer multiple requests in a row. 

import socket

HOST = "127.0.0.1" 
PORT = 65432  

print("server starting - listening for connections at IP", HOST, "and port", PORT,"\n")

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print(f"could not create socket\n")

try:
    s.bind((HOST, PORT))
except:
    print(f"binding error\n")

# responds to the given data by matching one of the client's specific questions with the correct answer. encodes the response and 
# sends it back to the client. prints progress messages as the data is recieved and sent back. 
def respond(data):
    print(f"received client message: '{data!r}' [{len(data)} bytes]\n")
    decoded_data = data.decode("utf-8")
    operation = ""

    if decoded_data == "List the best dining halls at Smith":
        response = "Cutter, Haynes, and Nogi"
        operation = "list"
    elif decoded_data == "What is the best Haynes Stir Fry sauce":
        response = "Gochujuang"
        operation = "best"
    elif decoded_data == "What are the dinner hours":
        response = "5pm - 7pm"
        operation = "hours"
    else: 
        response = "That request is not known."

    print("requested operation is \"", operation, "\"\n" )
    print("sending result message '", response ,"' back to client")
    conn.sendall(response.encode("utf-8"))


s.listen()
conn, addr = s.accept() 
with conn: 
    print(f"connection established with {addr}\n") 
    while True:
        data = conn.recv(1024) 
        if not data: 
            break
        respond(data)
        print("server is done!\n")

s.close()
