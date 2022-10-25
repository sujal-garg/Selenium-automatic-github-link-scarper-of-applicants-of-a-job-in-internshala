#Importing all the necessary selenium lib after pip installing selenium in command propmt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import time


#Creating a login bot using selenium
#Adding your Eamil Credentials for Login
internshala_mail = "#enter email id"
internshala_pass = "#enter pass"

#Setting up Chrome driver path 
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#URL of the website and webpage we want to visit
driver.get("https://www.internshala.com/")
driver.get("https://internshala.com/student/dashboard")

#Inspecting the email feild
email =  driver.find_element(By.NAME, "email")
email.send_keys(internshala_mail)

#Inspecting the password feild
password = driver.find_element(By.NAME, "password")
password.send_keys(internshala_pass)
password.send_keys(Keys.RETURN)


#Creating a bot to selecting the profile button using selenium
driver.find_element(By.XPATH("#xpath of the button to be entered")).click();

# identify elements with tagname <a>
lnks=driver.find_elements_by_tag_name("a")
# traverse list
for lnk in lnks:
   # get_attribute() to get all href
   print(lnk.get_attribute(href))
driver.quit()