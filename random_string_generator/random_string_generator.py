#!/usr/local/bin/python2.7


# This script will generate a random string by combining random numbers with random letters
# This will be then output as a file 


######################################################################################
# Location of numbers file
######################################################################################
my_dict_file = open("numbers.txt", "r")
######################################################################################
# Location of output files
######################################################################################
folderPath = r"Generator/"


######################################################################################
### Function to create folder #########################################################
######################################################################################

import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


######################################################################################
# IMPORT SOCKET MODULE TO BE ABLE TO SHOW HOSTNAME 
######################################################################################

import socket
hostname = socket.gethostname()
# print (hostname)

######################################################################################
# CREATE FOLDER FOR CURRENT MACHINE ###########################################
######################################################################################

from os import mkdir
# mkdir(folderPath + hostname)
createFolder(folderPath + hostname)

# CREATE NEW OUTPUT FILE - In case file doesn't exist
output_file = open(folderPath + hostname + "/%s.txt" % hostname, "w")


######################################################################################
# Process numbers file
######################################################################################

# read the data using a text file
# then splitting the lines by the comma delimeter


allItems = my_dict_file.read().split(',')


for line in my_dict_file:
	l = [i.strip() for i in line.split(',')]
#   print line 
# 	Add each string to the array
# 	allItems.append(line)
	allItems.append(l)
#   print (line)


######################################################################################
# Letters list
######################################################################################

letterList = [ "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z" ]

######################################################################################
# DEBUG - CHECKING ARRAY HAS IMPORTED CORRECTLY #######################################
# print ("---------------------------------------------------------------------------")
# print ("PRINTING ALL ITEMS IN LIST")
# print ("---------------------------------------------------------------------------")
# print (allItems)
print ("---------------------------------------------------------------------------")
print ("NUMBER OF ITEMS IN numbers IS:")
print ("---------------------------------------------------------------------------")
print len(allItems)
# text_file.close()


######################################################################################
### SECTION TO SELECT AND COMBINE RANDOM STRINGS #####################################
######################################################################################

import random

######################################################################################
### DEBUG - TEST PRINT RANDOM CHOICE FROM ALL ITEMS ##################################
######################################################################################
# print(random.choice(allItems))

randomString1 = (random.choice(allItems))
randomString2 = (random.choice(allItems))
randomString3 = (random.choice(allItems))
randomString4 = (random.choice(allItems))


print ("---------------------------------------------------------------------------")
print ("PRINTING RANDOM STRING 1:")
print ("---------------------------------------------------------------------------")
print (randomString1)
print ("---------------------------------------------------------------------------")
print ("PRINTING RANDOM STRING 2:")
print ("---------------------------------------------------------------------------")
print (randomString2)
print ("---------------------------------------------------------------------------")
print ("PRINTING RANDOM STRING 3:")
print ("---------------------------------------------------------------------------")
print (randomString3)
print ("---------------------------------------------------------------------------")
print ("PRINTING RANDOM STRING 4:")
print ("---------------------------------------------------------------------------")
print (randomString4)
print ("---------------------------------------------------------------------------")
print ("PRINTING RANDOM STRING CONCATENATED:")
print ("---------------------------------------------------------------------------")
print (randomString1) + (randomString2) + (randomString3) + (randomString4)
print ("---------------------------------------------------------------------------")
print ("PRINTING RANDOM LETTER STRINGS:")
print ("---------------------------------------------------------------------------")
letterString1 = (random.choice(letterList))
letterString2 = (random.choice(letterList))
letterString3 = (random.choice(letterList))
print (letterString1)
print (letterString2)
print (letterString3)
print ("---------------------------------------------------------------------------")
print ("PRINTING RANDOM STRING CONCATENATED WITH LETTERS:")
print ("---------------------------------------------------------------------------")
outputString = (randomString1) + (randomString2) + (randomString3) + (randomString4) + (letterString1) + (letterString2) + (letterString3)
print (outputString)
print ("---------------------------------------------------------------------------")


######################################################################################
# CREATE SIMPLE BACKUP #################################################################
######################################################################################

print ('BACKING UP CURRENT FILE')
sourceFile = (folderPath + hostname + "/%s.txt" % hostname)
copiedFile = (folderPath + hostname + "/%s_old.txt" % hostname)

from shutil import copy2
copy2(sourceFile,copiedFile)


###################################################################################
# BACKUP CURRENT FILE AND AMMEND DATE #############################################
###################################################################################
# import os
# import datetime
# FilePath = (serverPath + hostname + "/%s.txt" % hostname)
# modifiedTime = os.path.getmtime(FilePath)
# 
# timeStamp = datetime.datetime.fromtimestamp(modifiedTime).strftime("%d-%b-%y-%H-%M-%S")
# os.rename(FilePath,FilePath+"_"+timeStamp)
# 
# print ('DEBUG *****************************************************************')
# print ('PRINTING: FilePath')
# print ('DEBUG *****************************************************************')
# print(FilePath)
# print ('DEBUG *****************************************************************')
# 



###################################################################################
###################################################################################
### WRITE STRING TO FILE 
print ('WRITING STRING TO FILE')

output_file.write(outputString)

###################################################################################
# DEBUG
###################################################################################
# NOW CHECK STRING HAS WRITTEN
# checkFile = open(output_file, 'r')
# checkFile = output_file.read
# checkFile = output_file.read()
# print("CHECK FILE IS:")
# print(checkFile)
# 
# 
# if checkFile == outputString :
#     result = 'STRINGS MATCH - WRITE HAS COMPLETED'
# else:
#     result = 'STRINGS DO NOT MATCH - WRITE HAS PRODUCED AN ERROR'
# print(result)


output_file.close()
print ('***********************************************************************')

print ('DEBUG *****************************************************************')
# print ('PRINTING: checkFile')
# print(checkFile)
print ('PRINTING: outputString')
print ('***********************************************************************')
print(outputString)
print ('***********************************************************************')
# print ('PRINTING: FilePath')
# print ('DEBUG *****************************************************************')


### CLOSE #########################################################################
output_file.close()
print ('***********************************************************************')





