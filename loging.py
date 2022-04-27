from selenium import webdriver
import pyautogui as auto
import time
import imgbbpy
import os
from Trans import MSG

#whatsapp signin
driver = webdriver.Firefox("geckodriver")
# driver = webdriver.Chrome("C:/Users/acer/Downloads/chromedriver.exe")
driver.get("https://web.whatsapp.com/")
#Screenshot
qrIm = auto.screenshot("qr-code.jpg")
#uploading qr
client = imgbbpy.SyncClient("dcfd0780cf11630f5439c90bed7c6525")
image = client.upload(file="qr-code.jpg")
print(MSG.Qrlink.format(image.url))
os.remove("qr-code.jpg")
#sleeping
time.sleep(15)
driver.close()
#moving to cloud
import cloud