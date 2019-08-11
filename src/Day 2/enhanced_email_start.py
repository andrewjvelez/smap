#see https://realpython.com/python-send-email/ for more details

#Bring in the functionality to send email via SMTP, to get the date, and to format emails with HTML
import smtplib
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Create the function
def SendAlertEmail(piName):
    """Function to send basic alert email to email address"""

    #Set up variables for From Address and To Address
    From = "SmapAlert@gmail.com"
    To = "Sami.Mansoor@schroders.com"

    #Set up variable for today's date
    today = date.today()

    #Create the container for the email message
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'SMAP - An issue has been reported for ' + piName
    msg['From'] = From
    msg['To'] = To

    #TODO: Format the body of the message with HTML
    html = ""

    #Attach the message part into the container
    msg.attach(MIMEText(html, 'html'))

    #Create an open connection to the email server
    s = smtplib.SMTP('smtp.gmail.com',587)

    #Initiate the connection
    s.ehlo()
    #Encrypt the connection
    s.starttls()
    #Re-initiate the connection
    s.ehlo()

    #Login the email server
    s.login('SmapAlert@gmail.com', 'Schroders1/')
    #Send the message
    s.sendmail(From, To, msg.as_string())

    #Close the connection
    s.quit()



#Call the function that was created
SendAlertEmail('17th Floor Coffee Machine')
