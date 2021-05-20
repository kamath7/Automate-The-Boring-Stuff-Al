from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://www.bigbasket.com/pd/100393567/red-bull-energy-drink-350-ml-can/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop')
elem1 = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/table/tbody/tr[1]/td[2]')
print(elem1.text)