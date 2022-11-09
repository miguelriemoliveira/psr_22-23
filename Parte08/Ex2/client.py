#!/usr/bin/env python
# --------------------------------------------------
# Miguel Riem Oliveira.
# PSR, September 2020.
# Adapted from https://stackabuse.com/basic-socket-programming-in-python/
# -------------------------------------------------
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create TCP/IP socket
local_hostname = socket.gethostname()  # retrieve local hostname
local_fqdn = socket.getfqdn()  # get fully qualified hostname
ip_address = socket.gethostbyname(local_hostname)  # get the according IP address

server_address = (ip_address, 23456)  # bind the socket to the port 23456, and connect
sock.connect(server_address)
print ("connecting to %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))


# Define a dog to be sent
import dog_lib

dog = dog_lib.Dog('Dalila', 'brown', 5, 'Henrique')
dog.addBrother('Rex')
dog.addBrother('Zeus')
dog.addBrother('Rex')
dog.addBrother('Rex')
dog.addBrother('Rex')
dog.addBrother('Rex')
dog.addBrother('Rex')
dog.addBrother('Rex')
dog.addBrother('Rex')
print(dog)

# define example data to be sent to the server
# messages = [30, 'Robotics', 31, 14, 'Automation', 18]

# Serialization or marshalling
message = dog.name
message += ','
message += dog.owner
message += ','
message += str(dog.age)
message += ','
message += dog.color

for brother in dog.brothers:
    message+= ',' + brother

# Send the message

while True:
    print ('Sending message: ' + str(message))
    sock.sendall(message)
    time.sleep(2)  # wait for two seconds

sock.close()  # close connection
