import smtplib

smtpUser = 'raspberrypi.schroders@gmail.com'
smtpPass = 'Schroders1/'

toAdd = 'smansoor495@gmail.com'
fromAdd = smtpUser

subject = 'Python Test'
header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject : ' + subject
body = 'Some words here'

print (header + '\n' + body)

s = smtplib.SMTP('smtp.gmail.com',587)

s.ehlo()
s.starttls()
s.ehlo()

s.login(smtpUser, smtpPass)
s.sendmail(fromAdd, toAdd, header + '\n\n' + body)

s.quit()