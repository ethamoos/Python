
# Import mysql.connector which is the module which can connect to mysql

import mysql.connector as mysql

# Populate with details to connect to the server 
# NOTE - ensure that your servers are secure as access to this details provides access to the server
db = mysql.connect(
  host="mysqlServer.com",
  user="databaseUser",
  passwd="myPassword",
  database="nameOfDatabase"
)

cursor = db.cursor()


##########################################################################################
# GET HOSTNAME
##########################################################################################

import socket

hostname = socket.gethostname()

print ("Updating host:", hostname)

##########################################################################################
# GET CURRENT USER
##########################################################################################

import os

# Gives user's home directory
userhome = os.path.expanduser('~')          

# Gives username by splitting path based on OS
print ("Current username is: " + os.path.split(userhome)[-1] )
username = os.path.split(userhome)[-1]

# print (username)


##########################################################################################
# defining the Query
##########################################################################################

# The name of the table we are updating is "computers"
# The query updates the record to the current username and state - matching to the record from the name column

query = "UPDATE computers SET state = %s WHERE name = %s"
query2 = "UPDATE computers SET currentuser = %s WHERE name = %s"

# storing values in a variable objects
values = ("on",hostname)
values2 = (username,hostname)


# executing the query with values provided by the values object
cursor.execute(query, values)
cursor.execute(query2, values2)

# Now tell the database that we have changed the table data
db.commit()



