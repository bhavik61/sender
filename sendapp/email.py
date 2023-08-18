import smtplib

def send(emailList, subject, message, emailSender, emailSenderPassword, smtpVar):
	smtpObj = smtplib.SMTP(smtpVar, 587)
	smtpObj.ehlo()
	smtpObj.starttls()

	smtpObj.login(emailSender, emailSenderPassword) 
	smtpObj.sendmail(emailSender, emailList,'Subject:' + subject + '\n' + message)

	smtpObj.quit()