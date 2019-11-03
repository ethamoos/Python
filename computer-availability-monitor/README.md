# Computer availability monitor

This is a project based on an idea by James Durler. The purpose is to be able to monitor the current availability of a group of computers in a public open-access area, via a simple web page. This is achieved via a Python script which runs on the clients at regular intervals and reports data to a mysql database. A website then serves a web page which displays the data in realtime. This was built initially to run on Apple Macs and Linux clients but because it uses Python it could potentially also run on Windows.

The website displays the following information for each device:

Name:			hostname of device
Status:		if online
Current user:		name of current user, or noone logged in
Last response:	last time device “checked in”

These are the current attributes being reported but this can be configured to report on any available attribute, if required, limited only by the design of the current web page.

—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

This project requires the following:

web service - built using apache web server with php installed to host local facing web site. 

mysql server and database - the data is uploaded to mysql

method to run Python script on clients at regular intervals. This could be configured on the clients via a background service like cron, or be run via a management system/agent at regular intervals. 

—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————


NOTE - This project is designed for being running within a local network and with appropriate security hardening configured, as required. Ensure that your servers are secure.
