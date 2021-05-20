from typing import Text
from selenium import webdriver
import time
from message import message

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://web.whatsapp.com")
input("Press any key to continue")

def send(msg,phonen):
    driver.get(f"https://web.whatsapp.com/send?phone=91{phonen}")
    time.sleep(10)
    
def image(msg):   
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div').click()
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button/input').send_keys("/home/amalpaul/Development/Python/whatsappbot/image.jpeg")
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]').send_keys(msg)
    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/span/div').click()

    
def text(msg): 
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(msg)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()

def send(msg,phonen):
    driver.get(f"https://web.whatsapp.com/send?phone=91{phonen}")
    time.sleep(7)
    image(msg)
    time.sleep(5)

with open('./phoneno.csv','r')as myfile:
    while myfile:
        phoneno  = myfile.readline()
        if phoneno == "":
            print("All Messages Sent")
            break
        send(message,phoneno)
        print(phoneno)



