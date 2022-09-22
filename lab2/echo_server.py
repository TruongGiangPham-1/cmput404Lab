#!/usr/bin/env python3
import socket
import time
from multiprocessing import Process
#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept() # conn = socket, addr = ip , outgoing port of the client to s
            print("Connected by", addr)
            


            # create new process
            # p = Process(target = echo_handler, args=(conn, addr))
            #p.daemon = true
            #
            p = Process(target = echo_handler, args=(conn, addr))
            p.start()
            conn.close()
            # one connection is made, create new socket
            # with socket.socket  ... as s1:
                 # 
                 # after sending it to google, we shutdown so c
                 # we read the data we got back(using while loop)
                 # then we send what we got back to the proxy client
            #recieve data, wait a bit, then send it back
            #full_data = conn.recv(BUFFER_SIZE)
            #time.sleep(0.5)
            #conn.sendall(full_data)
            #conn.close()


# demo of what to do in echo server with fork

def echo_handler(conn, addr):
    full_data = conn.recv(BUFFER_SIZE)
    time.sleep(0.5)
    conn.sendall(full_data)
    conn.close()   

if __name__ == "__main__":
    main()
