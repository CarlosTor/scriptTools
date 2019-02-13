#!/usr/bin/python
import smtplib

def sendEmail(time=0):
    sender = 'SENDER_EMAIL'
    receivers = ['RECEIVER_EMAIL_1','RECEIVER_EMAIL_2','RECEIVER_EMAIL_3',...]

    message =  'From: SENDER_NAME <SENDER_EMAIL> \n'
    message += 'To: RECEIVER_NAME <RECEIVER_EMAIL> \n'
    message += 'Subject: YOUR_SUBJECT \n'

    message += 'YOUR_MESSAGE'

    try:
       smtpObj = smtplib.SMTP('SERVER_EMAIL')
       smtpObj.sendmail(sender, receivers, message)
       print 'Successfully sent email'
    except SMTPException:
       print 'Error sending email'
