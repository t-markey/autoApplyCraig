from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from pathlib import Path
from email.mime.application import MIMEApplication
from os import path
# with help from codewithmosh.com
# and http://linuxcursor.com/python-programming/06-how-to-send-pdf-ppt-attachment-with-html-body-in-python-script


def sendingMail(yourName, yourEmail, namePostingSubject, yourPassword, yourResume, sendingTo, bodyBody):
    testingEmail = MIMEMultipart()
    testingEmail["from"] = yourName
    testingEmail["to"] = sendingTo
    testingEmail["subject"] = namePostingSubject
    testingEmail.attach(
        MIMEText(bodyBody))
    with open(yourResume, "rb") as f:
        # attach = email.mime.application.MIMEApplication(f.read(),_subtype="pdf")
        attach = MIMEApplication(f.read(), _subtype="pdf")
        # **** PLAY WITH THIS TO FIX NAME OF PDF BEING SENT
        attach.add_header('Content-Disposition',
                          'attachment', filename=path.basename(yourResume))
        testingEmail.attach(attach)

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        # starting of client and smtp server for GMAIL as is
        smtp.starttls()
        # all commands going to server encrypted
        smtp.login(yourEmail, yourPassword)
        smtp.send_message(testingEmail)
        print("sent email....")


# use this to test before going live, sub practice email with your own
# list = ["testemails@gmail.com",
#         "testemail@gmail.com", "testemail@gmail.com"]

# for g in list:
#     sendingMail("Your Name", "YOUREMAIL@gmail.com", "Applying to your Posting",
#                 "YOURPASS", "samples.pdf", g, "body")
