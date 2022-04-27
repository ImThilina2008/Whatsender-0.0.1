import subprocess as ter
from Trans import MSG 

print(MSG.installing)
#installing,update and setuping envoirment 
ter.run("apt update")
ter.run("apt install pip")
ter.run("pip install wget")
ter.run("pip install imgbbpy")
ter.run("pip install selenium")
ter.run("pip install pyautogui")
# ter.run("cd")
# ter.run("mkdir Whatsender")
# ter.run("cd Whatsender")
ter.run("mkdir Down")
ter.run("mkdir Split")
ter.run("pip install filesplit")
# ter.run("wget https://download1647.mediafire.com/r9m66urnkqdg/zqxk0v37dgmgjek/geckodriver")

#moving to Whatsapp logging
import logging