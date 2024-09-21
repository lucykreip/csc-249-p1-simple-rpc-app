## Client Trace
client starting - connecting to dining server at IP 127.0.0.1 and port 65432 

connection established, sending request 'List the best dining halls at Smith'

message sent, waiting for reply

meceived response: 'b'Cutter, Haynes, and Nogi.'' [25 bytes]

client is done!

connection established, sending request 'What is the best Haynes Stir Fry sauce'

message sent, waiting for reply

meceived response: 'b'Gochujuang.'' [11 bytes]

client is done!

connection established, sending request 'What are the dinner hours'

message sent, waiting for reply

meceived response: 'b'5pm - 7pm'' [9 bytes]

client is done!

## Server Trace
server starting - listening for connections at IP 127.0.0.1 and port 65432 

connection established with ('127.0.0.1', 56939)

received client message: 'b'List the best dining halls at Smith'' [35 bytes]

requested operation is " list "

response is ' Cutter, Haynes, and Nogi. '

server is done!

received client message: 'b'What is the best Haynes Stir Fry sauce'' [38 bytes]

requested operation is " best "

response is ' Gochujuang. '

server is done!

received client message: 'b'What are the dinner hours'' [25 bytes]

requested operation is " hours "

response is ' 5pm - 7pm '

server is done!