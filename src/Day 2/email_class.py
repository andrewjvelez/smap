#see https://realpython.com/python-send-email/ for more details

#Bring in the functionality to send email via SMTP, to get the date, and to format emails with HTML
import smtplib
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#define the ServiceAlert class
class ServiceAlert():

	#the __init__ function is used to initialize class variables
	#the "self" object is a container for variables internal to the class
	def __init__ (self, piName = '17th Floor Coffee Machine'):
		self.sender = "SmapAlert@gmail.com"
		self.to = "andrewjvelez@gmail.com"
		self.mailServerName = 'smtp.gmail.com'
		self.mailServerPort = 587
		self.mailServerUserName = 'SmapAlert@gmail.com'
		self.mailServerUserPassword = 'Schroders1/'
		self.message = ""
		self.piName = piName
		
	#Create a method to change the default recipient	
	def SetRecipient(self, emailAddress):
		self.to = emailAddress
		
	#Set a custom message
	def SetMessage(self, emailMessage):
		#Update the message
		self.message = emailMessage
		
	#reset the message
	def UseDefaultMessage(self):
		#clear the message variable
		self.message = ""
	
	def BuildMessage(self):
		#Set up variable for today's date
		today = date.today()
		if self.message == "":
			return("""\
				<html>
					<h1><b>An issue has been reported for """ + str(self.piName) + """ </b></h1>
					<p>A user has reported the issue on """ + str(today) + """</p>
					<p>Please troubleshoot """ + str(self.piName) + """ at your earliest convenience.</p>
				</html>
				""")
		else:
			return (self.message)
		
	#Create the method to send an email
	def SendEmail(self):
		"""Function to send basic alert email to email address"""

		#Create the container for the email message
		msg = MIMEMultipart('alternative')
		msg['Subject'] = 'SMAP - An issue has been reported for ' + self.piName
		msg['From'] = self.sender
		msg['To'] = self.to

		#Format the body of the message with HTML
		html = self.BuildMessage()

		#Attach the message part into the container
		msg.attach(MIMEText(html, 'html'))

	   #Create an open connection to the email server
		s = smtplib.SMTP(self.mailServerName, self.mailServerPort)

		#Initiate the connection
		s.ehlo()
		#Encrypt the connection
		s.starttls()
		#Re-initiate the connection
		s.ehlo()

		#Login the email server
		s.login(self.mailServerUserName, self.mailServerUserPassword)
		#Send the message
		s.sendmail(self.sender, self.to, msg.as_string())

		#Close the connection
		s.quit()




