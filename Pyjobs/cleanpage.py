from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.common.exceptions import NoSuchElementException
import emailtesting as e
import sys
browser = webdriver.Chrome()


class Apply:

    def closing(self, timeOpen):
        print(f"Closing Chrome in {timeOpen}seconds...")
        time.sleep(timeOpen)
        browser.quit()
        return
        # function to set value of how long browser takes to close

    def scrapePosting(self, jobSection):
        global numberPostings, name, jobs

        response = requests.get(jobSection)
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.select(".result-row")
        name = soup.select(".result-title")
        numberPostings = len(jobs)

        # counts how many postings there are on page
    def getEmails(self, applyThisMany=0):
        emailList = []
        global numberPostings
        x = 0
        if applyThisMany > 0:
            # print(applyThisMany)
            numberPostings = applyThisMany + 1
         # lets input of how many postings to apply for , starts top of page
        else:
            print("no input")
        while x < (numberPostings - 1):
            # prints index , identifier, and link
            # print(x+1, jobs[x].get("data-pid", 0), name[x].get("href"))
            x += 1
            # opens current webpage
            browser.get(name[x].get("href"))
            try:
                buttonPressing = browser.find_element_by_xpath(
                    "//button[@role='button']")
                # finds button path
                if buttonPressing.is_displayed():
                    # checks if button is on page
                    browser.execute_script(
                        "arguments[0].click();", buttonPressing)
                    # press the button
                    time.sleep(7)
                    # delay to allow pressing
                    email = browser.find_element_by_class_name("mailapp")
                    # find the emaail in anchor element
                    # print(email.text)
                    print("Email Aquired")
                    # prints the text contained in the email link
                    emailList.append(email.text)
                    # add emails to a list
            except NoSuchElementException:
                print("No reply information")
        noRepeat = list(set(emailList))
        # uses sets to exclude repeat emails
        return noRepeat


a = Apply()
a.scrapePosting(
    "https://newyork.craigslist.org/d/food-beverage-hospitality/search/fbh")
emails = a.getEmails(4)
a.closing(2)
print("Number of emails aquired: ", len(emails))


# this takes arguments for your name, email , subject, password, resume name, sendee(supplied as g)
# for g in emails:
#     e.sendingMail("tom", "YOUREMAIL@gmail.com", "Applying to your Posting",
#                   "YOURPASSWORD", "samples.pdf", g)
#     print("Sent resume to", g)
