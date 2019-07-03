#Bring in the functionality to send email via SMTP
import smtplib

#Create the function
def SendAlertEmail():
	"""Function to send basic alert email to email address"""
	#define the account to send the email from. 
	#smtpUser = 'raspberrypi.schroders@gmail.com'
	#smtpPass = 'Schroders1/'
	smtpUser = 'SmapAlert@gmail.com'
	smtpPass = 'Schroders1/'
	smtpServer = 'smtp.gmail.com'

	#define who will receive the email
	toAdd = 'andrew.velez@schroders.com'
	#set the from address. 
	#Note that the "From" address could be another address
	fromAdd = smtpUser

	#Set the email subject
	subject = 'Python Test'
	#Set the email header
	header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject : ' + subject
	#Define the body
	body = 'Some words here'

	#Show the header and body on the console
	print (header + '\n' + body)

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
	#Send the message
	s.sendmail(fromAdd, toAdd, header + '\n\n' + body)

	#Close the connection
	s.quit()



#Call the function that was created
SendAlertEmail()
