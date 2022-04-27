from Trans import MSG
import pywhatkit as kit
from FileData import Data 
import sele
from selenium import webdriver
import time 

WhatsName = input(MSG.whatneo)
print(MSG.upload)
NameList = Data.Chunknames.copy()
FileIndex = 0
ChunkV = Data.Chunks+1
FileNo = 1
filepath = f"Split/{NameList[FileIndex]}"

while FileNo<ChunkV:
    driver = webdriver.Firefox("geckodriver")
    driver.get("https://web.whatsapp.com/")


    user = driver.find_element_by_xpath("//span[@title = '{}']".format(WhatsName))
    user.click()

    ABox = driver.find_element_by_xpath("//div[@title = 'Attach']")
    ABox.click()

    DocBox = driver.find_element_by_xpath("//input[@acept = '*']")
    DocBox.send_keys()

    time.sleep(2)

    Sent = driver.find_element_by_xpath("//div[@data-icon = 'send']")
    Sent.click()

    FileNo += 1 
    FileIndex += 1

print(MSG.Done)
import clear

