# Verify
Useful snippets of python code for accessing Piwik

skeleton.py is the bare bones for accessing the api

ipAndService.py gets the ip address, service, visit count, days since first visit etc

to_sheets uses the google drive api to update a google sheet to a dataframe
 - To use the drive api you need to set up your credentials in https://console.developers.google.com
 - Set up a new project
 - Set up credentials
 - Click on service account key
 - Click create service account
 - Add a name and select the role as servcie owner
 - Chooe the defautl JSON option
 - Click create 
 - Copy the dowloaded file to your project folder and rename it client_secret.json
 - Open the file and copy the 'client_email' 
 - Share the sheet you want to update with this client-email
