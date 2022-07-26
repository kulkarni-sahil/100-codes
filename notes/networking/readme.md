# Networking In Python

## Sockets

<pre>
import socket

# creates an socket object 
# socket.AF_INET -> across the internet
# socket.SOCK_STREAM -> stream of data instead of block
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# data.pr4e.org -> host
# 80 -> Port
# this line can blow up
mysock.connect(('data.pr4e.org', 80))

