from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time
from datetime import datetime

driver = webdriver.Chrome('/home/prajip/Documents/chromedriver') 
driver2= webdriver.Chrome('/home/prajip/Documents/chromedriver')
driver.get("https://web.whatsapp.com/")
driver2.get("https://web.hike.in/")
wait = WebDriverWait(driver, 600) 
wait2 = WebDriverWait(driver2, 600)

# Target user
target = '"Adarsh K skct"'
target2 = '"Natasha"'

time.sleep(10) # time to load the page
x_arg = '//span[contains(@title, ' + target + ')]'
x_arg2 = '//span[contains(text(), ' + target2 + ')]'

time.sleep(15)
print(x_arg2)
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title2 = wait2.until(EC.presence_of_element_located((By.XPATH, x_arg2)))
group_title.click()
group_title2.click()

def sendMessage(mssg):
    inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@dir="ltr"][@data-tab="1"]'
    input_box = wait.until(EC.presence_of_element_located(( 
        By.XPATH, inp_xpath)))
    input_box.send_keys(mssg + Keys.ENTER)

def sendMessageToNat(mssg):
    inp_xpath1 = '//div[contains(@class, "selectable textArea lt_l7 messageBox")]'
    input_box_1 = wait2.until(EC.presence_of_element_located((
        By.XPATH, inp_xpath1)))
    input_box_1.send_keys(mssg + Keys.ENTER)

def getMessageFromNat():
    msg_path1 = '//div[@class="selectable h5_i1"]//span[@class="selectable qp_qs"]'
    all_mssgs1 = driver2.find_elements_by_xpath(msg_path1)
    a1 = all_mssgs1[0].text
    print("Debugging")
    print(a1)
    if "Stop" in str(a1):
        a1 = "Okay Bye then"
    if a1[0] != "$":
        mssg1 = "" + str(a1)
        sendMessage(mssg1)
    time.sleep(3)
    getMessage()
     
def getMessage():
    msg_path = '//div[@class="_3zb-j"]//span[@class="_3FXB1 selectable-text invisible-space copyable-text"]'
    all_mssgs = driver.find_elements_by_xpath(msg_path)
    a = all_mssgs[-1].text
    # b = all_mssgs[-2].text
    if a[0] != "$":
        mssg = " " +  str(a)
        sendMessageToNat(mssg)
    time.sleep(1)
    getMessageFromNat()

print("ON")
time.sleep(15) # time to load contents
getMessage()
