
#!/usr/bin/env python3
import socket
import time

#define address & buffer size
HOST = "127.0.0.1"
PORT = 8001
BUFFER_SIZE = 1024

def main():
    buffer_size = 4096
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

            
            
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
                hostGoogle = 'www.google.com'
                port = 80  # for google
            # one connection is made, create new socket
            # with socket.socket  ... as s1:
                 # 
                 # after sending it to google, we shutdown so c
                 # we read the data we got back(using while loop)
                 # then we send what we got back to the proxy client
            #recieve data, wait a bit, then send it back

                #s1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # set 1 -> 0 if there problem
                # SOL_SOCKET sets level, so reuse only applies to this s1 socket

                remote_ip = get_remote_ip(hostGoogle) # ip of google.com

                s1.connect((hostGoogle , port))  # connect to google
                print (f'Socket Connected to {hostGoogle} on ip {remote_ip}')

                full_data = conn.recv(BUFFER_SIZE)  # read from proxyClient
                print("got from proxyclient", full_data)
                time.sleep(0.5)



                # now relay data to google
                #send the data and shutdown
                print("full_data is, ", full_data.decode("utf-8"))
                send_data(s1, full_data.decode("utf-8") )  # turn byte to string, b'' to ''
                s1.shutdown(socket.SHUT_WR)  # google knows that there is no more to listn to so it can respond back


                # now get data from google to google
                full_data = b""
                while True:
                    data = s1.recv(buffer_size)
                    if not data:
                        break
                    full_data += data
                print(full_data)
                # 

                conn.sendall(full_data)
                conn.close()


# demo of what to do in echo server with fork
#create a tcp socket
def create_tcp_socket():
    print('Creating socket')
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except (socket.error, msg):
        print(f'Failed to create socket. Error code: {str(msg[0])} , Error message : {msg[1]}')
        sys.exit()
    print('Socket created successfully')
    return s

#get host information
def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    print (f'Ip address of {host} is {remote_ip}')
    return remote_ip

#send data to server
def send_data(serversocket, payload):
    print("Sending payload")    
    try:
        serversocket.sendall(payload.encode())
    except socket.error:
        print ('Send failed')
        sys.exit()
    print("Payload sent successfully")

def echo_handler(conn, addr):
    full_data = conn.recv(BUFFER_SIZE)
    time.sleep(0.5)
    conn.sendall(full_data)
    conn.close()   

if __name__ == "__main__":
    main()
