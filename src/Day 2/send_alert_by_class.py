from email_class import ServiceAlert

#"Instantiate" a service alert class
default_alert = ServiceAlert()

#We'll create another instance where we change some of the values
custom_alert = ServiceAlert("16th Floor Water Cooler")
custom_alert.SetRecipient("andrewjvelez@icloud.com")
custom_alert.SetMessage("Please check out the water machine on 16")

#send the email for the default
default_alert.SendEmail()
#send the email for the custom
custom_alert.SendEmail()

#now, let's reset the message for the custom alert and retest
custom_alert.UseDefaultMessage()
custom_alert.SendEmail()
