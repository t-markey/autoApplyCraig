import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import webbrowser
import emailtesting as emm
from os import path
import cleanpage as cl
import uslinks
import time
from PIL import ImageTk, Image


goo = tk.Tk(className=' AutoCraig 4000')
goo.geometry('560x660')
canvas = Canvas(goo, width=200, height=80)
canvas.grid(row=0, column=1)

x = 'Resume.pdf'
howmany = 4
location = str
masterInfo = []
regions = uslinks.regionalUsList
img = PhotoImage(file="autocraig4000.png")
canvas.create_image(0, 0, anchor=NW, image=img)


def callback(url):
    webbrowser.open_new(url)


# Status bar for sending emails

progress = ttk.Progressbar(
    goo,  orient=HORIZONTAL, length=100)
progress.config(mode='determinate', maximum=100)
progress.grid(row=17, column=1)


def stepping(inputs):
    # progress.step(inputs)
    progress['value'] = inputs
    # This is very important tkinter waits..
    progress.update_idletasks()
    goo.update_idletasks()
    progress.update()
    goo.update()


def sendingdata():
    global masterInfo
    global howmany
    global location
    masterInfo.clear()
    data1 = enterFirst.get()
    data2 = enterLast.get()
    data3 = enterEmail.get()
    data4 = enterPass.get()
    data5 = enterSubject.get()
    data6 = enterBody.get()
    data7 = enterHowmany.get()
    data8 = regionVar.get()

    masterInfo.append(data1 + " " + data2)  # name
    masterInfo.append(data3)  # email
    masterInfo.append(data5)  # Subject
    masterInfo.append(data4)  # email pass
    masterInfo.append(x)  # resume location..
    howmany = data7  # elemnts of list to iterate over ( g is variable)
    masterInfo.append(data6)  # body of email
    location = data8
    print('testing')
    #print('List:', masterInfo)
    print(location)
    return


def sendtestemail():
    sendingdata()
    # checks to make sure a resume is uploaded before sending
    if x == 'Resume.pdf':
        tk.messagebox.showerror(
            title=None, message='Please upload your Resume first before proceeding!')
        print(enterFirst.get())
        return
    # makes sure all fields are filled in
    # CAN ADD MORE MESSAGES TO FOCUS IN ON ISSUES, make sure @gmail is there
    if enterFirst.get() == '' or enterLast.get() == '' or enterEmail.get() == '' or enterPass.get() == '' or enterSubject.get() == '' or enterBody.get() == '' or str(enterHowmany.get()) == '0':
        tk.messagebox.showwarning(
            title=None, message='Fill in all of the fields before proceeding.')
        return
    # testing list..
    list1 = []
    print(howmany)
    howmanyINT = int(howmany)
    for q in range(howmanyINT):
        list1.append(masterInfo[1])
    counter = 0
    for g in list1:
        # progress.update_idletasks()
        time.sleep(1)
        emm.sendingMail(masterInfo[0], masterInfo[1], masterInfo[2],
                        masterInfo[3], x, g, masterInfo[5])
        counter += 1
        steps = counter * 100/howmanyINT
        stepping(steps)

    print('Testing function')
    print(path.basename(masterInfo[5]))
    stepping(0)
    return


def getresumefromfile(event=None):
    filename = filedialog.askopenfilename()
    print('Uploading your resume', filename)
    global x
    x = filename


def finalsend():
    global howmany
    sendingdata()
    a = cl.Apply()
    a.scrapePosting(
        "https://" + location + ".craigslist.org/d/food-beverage-hospitality/search/fbh")
    emails = a.getEmails(int(howmany))
    print("Number of emails aquired: ", len(emails))
    send to all
    for g in emails:
        emm.sendingMail(masterInfo[0], masterInfo[1], masterInfo[2],
                        masterInfo[3], x, g, masterInfo[5])
    a.closing(2)

    return


def sendtoallofus():
    howmany = 100  # can change to less for testing
    sendingdata()
    for allofit in uslinks.regionalUsList:
        location = allofit
        print(location)
        a = cl.Apply()
        a.scrapePosting(
            "https://" + location + ".craigslist.org/d/food-beverage-hospitality/search/fbh")
        emails = a.getEmails(int(howmany))
        print("Number of emails aquired: ", len(emails))
        for g in emails:
            emm.sendingMail(masterInfo[0], masterInfo[1], masterInfo[2],
                            masterInfo[3], x, g, masterInfo[5])

    a.closing(2)
    return


# Text to explain input boxes
Label(goo, text='').grid(row=0)
Label(goo, text='First Name').grid(row=1)
Label(goo, text='Last Name').grid(row=2)
Label(goo, text='Email(include @gmail.com)').grid(row=3)
Label(goo, text='Email Password').grid(row=4)
Label(goo, text='Subject of Email').grid(row=5)
Label(goo, text='Body of Email').grid(row=6)
Label(goo, text='Apply to 1-100 jobs').grid(row=7)
Label(goo, text='Choose region').grid(row=8)
# field of work?
Label(goo, text='').grid(row=10)  # empty place holder
Label(goo, text='').grid(row=14)  # empty place holder


# Links to support
linkHelp1 = Label(
    goo, text='Link to Enable 3rd Party apps in Gmail', fg="blue", cursor="hand1")
linkHelp1.grid(row=18, column=1)
linkHelp1.bind(
    "<Button-1>", lambda e: callback("https://support.google.com/mail/thread/10206863?hl=en"))
linkHelp2 = Label(
    goo, text='Link for help installing Chromium Driver', fg="blue", cursor="hand1")
linkHelp2.grid(row=19, column=1)
linkHelp2.bind(
    "<Button-1>", lambda e: callback("https://chromedriver.chromium.org/downloads"))

# creates input boxes
enterFirst = Entry(goo)
enterLast = Entry(goo)
enterEmail = Entry(goo, show="*")
enterPass = Entry(goo, show="*")
enterBody = Entry(goo, width='20')
enterSubject = Entry(goo)
enterHowmany = Spinbox(goo, from_=1, to=100)
regionVar = StringVar(goo)
regionVar.set("newyork")  # default value
enterRegion = OptionMenu(goo, regionVar, *regions)

# arranges input boxes
enterFirst.grid(row=1, column=1)
enterLast.grid(row=2, column=1)
enterEmail.grid(row=3, column=1)
enterPass.grid(row=4, column=1)
enterSubject.grid(row=5, column=1)
# this needs work doesnt type from the center....
enterBody.grid(row=6, column=1, padx=5, pady=0, ipady=40)
enterHowmany.grid(row=7, column=1)
enterRegion.grid(row=8, column=1)
enterRegion.config(width='20')


# Buttons to send emails
buttonResumeGet = tk.Button(
    goo, text='Upload a pdf Resume', command=getresumefromfile)
buttonResumeGet.grid(row=9, column=1)
buttonTest = tk.Button(
    goo, text='Send a Test email to yourself', command=sendtestemail)
buttonTest.grid(row=11, column=1)
buttonSend = tk.Button(
    goo, text='Apply to jobs in your Region', command=finalsend)
buttonSend.grid(row=12, column=1)
buttonSend = tk.Button(
    goo, text='* Apply to 4000 jobs *', command=sendtoallofus)
buttonSend.grid(row=13, column=1)
buttonExit = tk.Button(goo, text='Quit Program', command=goo.destroy)
buttonExit.grid(row=20, column=1)


# __________________________________________________________
# __________________________________________________________


def main():
    goo.mainloop()


if __name__ == '__main__':
    main()
