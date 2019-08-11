#see https://realpython.com/python-send-email/ for more details

#Bring in the functionality to send email via SMTP
import smtplib

#Create the function
def SendAlertEmail():
	"""Function to send basic alert email to email address"""
	#define the account to send the email from. 
	smtpUser = 'SmapAlert@gmail.com'
	smtpPass = 'Schroders1/'
	smtpServer = 'smtp.gmail.com'

	#TODO: define who will receive the email
	
	#TODO: set the from address. 

	#TODO: Set the email subject


	#Set the email header
	header = 'To: ' #add recipient
	 + '\n' + 'From: ' #add sender 
	 + '\n' + 'Subject : ' #add subject
	#TODO: Define the body



	#TODO: Show the header and body on the console
	

	#Create an open connection to the email server
	s = smtplib.SMTP(smtpServer,587)

	#Initiate the connection
	s.ehlo()
	#Encrypt the connection
	s.starttls()
	#Re-initiate the connection
	s.ehlo()

	#Login the email server
	s.login(smtpUser, smtpPass)
	#TODO: Send the message
	#SAMPLE COMMAND: s.sendmail(fromAdd, toAdd, header + '\n\n' + body)

	#Close the connection
	s.quit()



#Call the function that was created
SendAlertEmail()
