#!/usr/bin/env python

#----------------------------------------------------------------------------------#
# Project : Dyna Socket                                                            #
# Script  : Client                                                                 #
# Author  : Mrinal Wahal                                                           #
# Website : http://www.dynacrux.de.vu/                                             #
#----------------------------------------------------------------------------------#

def main():
    print "-"*60
    print "WELCOME TO DYNASOCKET"
    print "-"*60
    
    from functions import commands, falsifier
    import socket, os, sys, threading, select

    host = raw_input("Enter Host : ")
    port = 8888
    connlist = []

    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print "Socket Successfully Created."
        connlist.append(s)
        s.connect((host,port))
        print "Connected With " + host + " : " + str(port)
        print "-"*60
        print 
    except socket.error, e:
        print "Error : " + str(e)
        s.close()
        print "We May Have a Problem, Houstan."
        sys.exit()

    def recieve():
        while True:
            try:
                incoming = s.recv(8192)
                if incoming == "Incoming Target.":
                    target = s.recv(8192)
                    falsifier(target,s)
                else:
                    print "\n<Server>" + incoming
                    continue
            except Exception, e:
                print "Error : " + str(e)
                break
                s.close()

    rt = threading.Thread(target = recieve)

    def send():
        while True:
            reply = raw_input("<You>")
            commands(reply,s,s)

    st = threading.Thread(target = send)

    rt.start()
    st.start()

if __name__ == '__main__':
    main()
