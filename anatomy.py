#!/user/bin/python

# Example python Script
#Imports system information
import sys
#Asks user for name
who = input("Who are you?")
#Finds system file name
argc = len(sys.argv)

if argc > 1:
    print('Too many args')
else:
    #Welcomes user
    who = who
    print ("hello", who)
#Displays file name and system path
print ('The name and file location:' + sys.argv[0])
