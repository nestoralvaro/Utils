#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib

"""
description:
    Utility for sending e-mails on python
    You can choose between sending these e-mails using the local SMTP server, or
        you can send the messages using GOOGLE mail SMTP server.
    Caution: These e-mails may appear on the "SPAM" folder.
author:
    nestoralvaro
"""
def getMailNames(mail_addrs):
    """
    Extracts the names (the string before the "@" sign) from a e-mail addresses.

    Args:
      mail_addrs: (string OR list of strings) e-mail address(es)
    """
    if isinstance(mail_addrs, list):
      names = [m[:m.find("@")] for m in mail_addrs]
      names = ", ".join(names)
    else:
      names = mail_addrs[:mail_addrs.find("@")]
    return names

def buildMessage(sender, receivers, subject, msg_body):
    """
    Uses the information to prepare the message

    Args:
      sender: (string) e-mail address for the sender of the e-mail
      receivers: (list) e-mail addresses for all the recipents of the e-mail
      subject: (string) subject of the e-mail
      msg_body: (string) body of the e-mail
    """
    # E-mail contents meta-data
    message = "From: {} <{}>\n"
    message += "To: {} <{}>\n"
    message += "MIME-Version: 1.0\n"
    message += "Content-type: text/html\n"
    message += "Subject: {}\n\n{}"
    message = message.format(getMailNames(sender), sender, \
        getMailNames(receivers), ",".join(receivers), \
        subject, msg_body)
    return message

def sendEmail(sender, receivers, message):
    """
    Sends the e-mail message using the local SMTP server

    Args:
      sender: (string) e-mail address for the sender of the e-mail
      receivers: (list) e-mail addresses for all the recipents of the e-mail
      msg: (string) message body for the e-mail to be sent
    """
    try:
       smtpObj = smtplib.SMTP('localhost')
       smtpObj.sendmail(sender, receivers, message)
       print "Successfully sent email"
    except Exception as e:
       print "Error: unable to send email", e

def sendGoogleEmail(sender, receivers, message, google_mail_password):
    """
    Uses the information to send the message using GOOGLE mail

    Args:
      sender: (string) e-mail address for the sender of the e-mail.
          This has to be a GOOGLE MAIL account
      receivers: (list) e-mail addresses for all the recipents of the e-mail
      msg: (string) message body for the e-mail to be sent
    """
    try:
       server = smtplib.SMTP('smtp.gmail.com:587')
       server.ehlo()
       server.starttls()
       # If the login fails, allow it here: https://www.google.com/settings/u/1/security/lesssecureapps
       server.login(sender, google_mail_password)
       server.sendmail(sender, receivers, message)
       server.quit()
       print "Successfully sent email"
    except Exception as e:
       print "Error: unable to send email", e

if __name__ == '__main__':
    # Person who sends the e-mail
    sender = u"MY_OWN_EMAIL_ADDRESS@gmail.com"
    # Recipients of this e-mail (one or more)
    receivers = ["MY_FRIEND_1@gmail.com", "MY_FRIEND_2@hotmail.com"]
    # Subject text of the e-mail
    subject = "Holaaaaa :-)"
    # Main body of the e-mail (can be HTML code)
    msg_body = """Hi There!  <h1>Hola</h1>\n\nCan you, <b>read this</b>\n<h2>E-mail?</h2>"""
    # Full message
    message = buildMessage(sender, receivers, subject, msg_body)
    # Send the e-mail using your local SMTP server
    #sendEmail(sender, receivers, message)
    # TODO: Put here your google mail (gmail) password
    google_mail_password = 'YOUR_GOOGLE_MAIL_ACCOUNT_PASSWORD'
    # Send the same e-mail using GOOGLE SMTP server.
    # TODO: make sure the "sender" is your google mail (gmail) account.
    sendGoogleEmail(sender, receivers, message, google_mail_password)
