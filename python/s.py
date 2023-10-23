#!/bin/python3

#SOCKETS 

import socket 

HOST = '127.0.0.1'
PORT = 7777

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM) #AF inet is ipv4 , sock_stream is a port
s.connect((HOST,PORT))
