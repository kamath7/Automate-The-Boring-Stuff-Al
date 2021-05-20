from selenium import webdriver
import time 

browser = webdriver.Firefox()
browser.get('https://google.com/')
elem = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/a')
elem.click()
elem1 = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div[1]/div[1]/div[1]/div/div[2]/input')
elem1.send_keys('adithya kamath')
elem1.submit()
time.sleep(30)
browser.close()
#other methods include - browser.close(), browser.refresh(), browser.back()