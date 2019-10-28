#----------------------------------------------------------------------------------#
# Project : Dyna Socket                                                            #
# Script  : Server                                                                 #
# Author  : Mrinal Wahal                                                           #
# Website : http://www.dynacrux.de.vu/                                             #
#----------------------------------------------------------------------------------#

print("-"*60)
print("WELCOME TO DYNASOCKET")
print("-"*60)

from functions import commands, falsifier
import socket, os, threading, sys

host = "0.0.0.0"
port = 8888
connlist = []

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket Successfully Created.")
    connlist.append(s)
    s.bind((host,port))
    print("Socket Successfully Binded.")
    s.listen(10)
    print("Socket is Now Listening.")
except Exception as e:
    print(f"Error : {str(e)}")
    os.system("pause")

try:
    ipreq = input("Do You Wish to See Your IP Configuration ? (Y/N) : ")
    if ipreq == "y" or ipreq == "Y":
        os.system("ipconfig")
    else:
        pass
except Exception as e:
    print(f"Error : {str(e)}")
    
try:
    conn, addr = s.accept()
    connlist.append(conn)
    print(f"Connected With {addr[0]} : {str(addr[1])}")
    print("-"*60)
    print("")
except Exception as e:
    print(f"Error : {str(e)}")
    

def recieve():
    while True:
        for sock in connlist:
            try:
                key = sock.recv(8196)
                if key == "Incoming Target.":
                    target = sock.recv(8192)
                    falsifier(target,sock)
                else:
                    print(f"\n< {str(addr[1])} > {key}")
            except socket.error as e:
                pass

recieveth = threading.Thread(target = recieve)
recieveth.start()
        
def send():
    while True:
        server_prompt = input("<You>")
        commands(server_prompt.encode('utf-8'),conn,s)

sendth = threading.Thread(target = send)
sendth.start()

s.close()