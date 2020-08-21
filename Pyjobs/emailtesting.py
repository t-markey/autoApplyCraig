from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from pathlib import Path
from email.mime.application import MIMEApplication
# with help from codewithmosh.com
# and http://linuxcursor.com/python-programming/06-how-to-send-pdf-ppt-attachment-with-html-body-in-python-script


def sendingMail(yourName, yourEmail, namePostingSubject, yourPassword, yourResume, sendingTo):
    testingEmail = MIMEMultipart()
    testingEmail["from"] = yourName
    testingEmail["to"] = sendingTo
    testingEmail["subject"] = namePostingSubject
    testingEmail.attach(
        MIMEText("Thanks for you consideration. My resume is attached"))
    with open(yourResume, "rb") as f:
        # attach = email.mime.application.MIMEApplication(f.read(),_subtype="pdf")
        attach = MIMEApplication(f.read(), _subtype="pdf")
        attach.add_header('Content-Disposition', 'attachment',
                          filename=yourResume)
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
# list = ["PracticeEmail@email", "PracticeEmail@email",
#         "PracticeEmail@email", "PracticeEmail@email", "PracticeEmail@email"]

# for g in list:
#     sendingMail("tom", "YourEmail@email.com", "Applying to your Posting",
#                 "YourPassword", "samples.pdf", g)
