import mechanize
import urllib2  #maybe python3
import urllib
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.common.keys import Keys
import threading
import os
import re
from bs4 import BeautifulSoup

#id_att = []
#issue_text = []
#filename = raw_input("Name of file you want issues saved to ")
#file = open(filename, 'w+')

#File Numbers to traverse
stfile = long(raw_input("Enter Folder Number you want to start at "))
endfile = long(raw_input("Enter Folder Number you want to end at "))

#UserName and PW
username = raw_input("Enter Incontact Username ")
password = raw_input("Enter Incontact password ")

#open browser  - spoof it using mechanize
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(False)
br.addheaders = [('User-agent', 'Firefox')]

#instantiate selenium browser object
url1 = "https://login.incontact.com"
url2 = "https://home-c9.incontact.com/inContact/Manage/FileManager/BrowseFiles.aspx"
browser = webdriver.Firefox()
browser.get(url2)

#---- Login ------
un = browser.find_element_by_name("ctl00$BaseContent$tbxUserName")
time.sleep(1)
un.send_keys(username)

#pw = browser.find_element_by_id("ctl00_BaseContent_tbxPassword.textfield").clear()
pw = browser.find_element_by_name("ctl00$BaseContent$tbxPassword")
time.sleep(1)
pw.send_keys(password + Keys.RETURN)

#----- click on folder ID -----------

#? what happens if its not visible
#//*[@id="ctl00_ctl00_ctl00_BaseContent_Content_FileManagerContent_tvDirectoryt181"]   #1259260000
#//*[@id="ctl00_ctl00_ctl00_BaseContent_Content_FileManagerContent_tvDirectoryt180"]   #1259250000
#//*[@id="ctl00_ctl00_ctl00_BaseContent_Content_FileManagerContent_tvDirectoryt179"]   #1259240000
#//*[@id="ctl00_ctl00_ctl00_BaseContent_Content_FileManagerContent_tvDirectoryt177"]   #1259220000
#//*[@id="ctl00_ctl00_ctl00_BaseContent_Content_FileManagerContent_tvDirectoryt142"]   #1250850000

#(125745 + x)*10000
folder_xpath_id_start = (stfile/10000) - 125745
folder_xpath_id_end = (endfile/10000) - 125745
for id in range(folder_xpath_id_start, (folder_xpath_id_end+1)):
    print id
    path = '#//*[@id="ctl00_ctl00_ctl00_BaseContent_Content_FileManagerContent_tvDirectoryt' + str(id) + '"]'
    fold = browser.find_element_by_name(path)

    # Check if button exists
    if fold.text == ' ':
        print("No Button" + str(id))
    else:
        fold.click()
        time.sleep(2)  
        delete = browser.find_element_by_name('//*[@id="ctl00_ctl00_ctl00_BaseContent_Content_FileManagerContent_btnDeleteDir_btnMain_ShadowButtonSpan"]')
        if delete.text == ' ':
            print("Cant Delete")
        else:
            delete.click()
            time.sleep(2)
            confirm = browser.find_element_by_name('//*[@id="ctl00_ctl00_ctl00_BaseContent_Content_FileManagerContent_btnDeleteDir_btnConfirmOk_ShadowButtonSpan"]')
            #confirm.click()
            


#----- AGENT ISSUES ------------
