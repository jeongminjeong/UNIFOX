# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome('C:/Users/정민정/Desktop/chromedriver_win32/chromedriver.exe')

driver.implicitly_wait(3) #3초 대기, 안 써도 됨

url = 'https://www.google.com/'
driver.get(url)

driver.find_element_by_id('lst-ib').click()
driver.find_element_by_id('lst-ib').send_keys('weather')
driver.find_element_by_name('btnK').click()
