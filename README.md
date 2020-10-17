# AutoCraig 4000

Apply to 4000 jobs with one click!

AutoCraig 4000 is a tool to automate emails to prospective employers. Specifically this tool has the capability to extract the contact emails from the 4000 most recent job listings on Craigslist in a given field of work. ( Currently using Food/ Bev/ Hospitality)

## Features
* Scrapes Craigslist for employer's contact email
* GUI to upload resume, fill in body, Subject of emails
* Select how many emails to send 1-4000
* Send a test email to yourself
* Select a specific region to target

## Examples

![GUI](/Pyjobs/examples/autocraig.png)



## Installation

Enable 3rd Party apps in  [gmail](https://support.google.com/mail/thread/10206863?hl=en) .

Install and setup  [chrome driver](https://chromedriver.chromium.org/downloads) .

Run gooey.py to open the GUI for inputting 
```python
python3 gooey.py
```

## Usage 
Input your credentials, fill in fields, and upload a resume. (samples.pdf is provided to use for testing). 

The region section is based on the craigslist url of that region .




## Credits
http://linuxcursor.com/python-programming/06-how-to-send-pdf-ppt-attachment-with-html-body-in-python-script

http://codewithmosh.com

## Known Issues
This program sets  chrome to headless mode allowing the web automation to be done in the background out of sight.  There is sometimes an issue of chrome being stuck in headless mode after using the program. Changing `browser = webdriver.Chrome(chrome_options=chrome_options)` to `browser = webdriver.Chrome()` in `cleanpage.py` and running that script works to revert chrome back to normal.  Alternatively , a cleaner way to do this:

```python
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium import webdriver
import sys

browser = webdriver.Chrome()
```

 

## License
[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)
