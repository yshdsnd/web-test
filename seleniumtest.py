#!/usr/bin/env python3

import time
from selenium import webdriver

desired_capabilities = {
    "xcodeOrgId": "9F678VWCFJ",
    "xcodeSigningId": "iPhone Developer",
    'browserName': 'Safari',
    'platformName': 'iOS',
    'platformVersion': '13.3',
    'deviceName': 'iPhone',
    'udid': '00008030-000104160C82802E'
}

#URL = 'https://www.yahoo.co.jp'
#URL = 'https://www.google.co.jp'
#URL = 'http://www.sokohiki.org/~yoshi/test/'

url = 'http://www.sokohiki.org/~yoshi/'
protected_url = 'http://www.sokohiki.org/~yoshi/test/'
username = 'test1'
password = 'password1'

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4723/wd/hub',
    desired_capabilities=desired_capabilities)
#driver = webdriver.Safari()

script_str = (
        "var XMLReq = new XMLHttpRequest();"
        "XMLReq.open('GET', '" \
        + protected_url + "', false, '" \
        + username + "', '" + password + "');"
        "XMLReq.send(null);"
)

driver.get(url)
print("Move to " + protected_url)
print("sleep 3seconds.")
time.sleep(3)

driver.execute_script(script_str)
driver.get(protected_url)

print("sleep 3seconds.")
time.sleep(3)
#time.sleep(10)
#driver.close()

driver.quit()
