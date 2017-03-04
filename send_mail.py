#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib

"""
description:
    Utility for sending e-mails on python using the local SMTP server.
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

def sendEmail(sender, receivers, message):
    """
    Sends the e-mail message using the provided sender and receiver(s)

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

if __name__ == '__main__':
    # Person who sends the e-mail
    sender = "me@localhost.com"
    # Recipients of this e-mail (one or more)
    receivers = ["MY_FRIEND_1@gmail.com", "MY_FRIEND_2@hotmail.com"]
    # Subject text of the e-mail
    subject = "Hola :-)"
    # Main body of the e-mail (can be HTML code)
    msg_body = """Hi There!  <h1>Hola</h1>\n\nCan you, <b>read this</b>\n<h2>E-mail?</h2>"""
    # Full message
    message = buildMessage(sender, receivers, subject, msg_body)
    # Send the e-mail
    sendEmail(sender, receivers, message)
