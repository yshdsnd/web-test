#!/usr/bin/env python3

import time
from selenium import webdriver

#URL = 'https://www.google.co.jp/'
#URL = 'http://test1:password1@www.sokohiki.org/~yoshi/test/'
url = 'http://www.sokohiki.org/~yoshi/'
protected_url = 'http://www.sokohiki.org/~yoshi/test/'
username = 'test1'
password = 'password1'

#driver = webdriver.Chrome()
#driver = webdriver.Edge()
driver = webdriver.Firefox()
driver.get(url)
print("Move to " + protected_url)
print("sleep 3seconds.")
time.sleep(3)
script_str = (
        "var XMLReq = new XMLHttpRequest();"
        "XMLReq.open('GET', '" \
        + protected_url + "', false, '" \
        + username + "', '" + password + "');"
        "XMLReq.send(null);"
)
driver.execute_script(script_str)
driver.get(protected_url)
print("sleep 3seconds.")
time.sleep(3)
driver.close()
driver.quit()
