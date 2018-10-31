# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome('C:/Users/정민정/Desktop/chromedriver_win32/chromedriver.exe')

driver.implicitly_wait(2)

url = 'https://www.youtube.com'
driver.get(url)

driver.find_element_by_id('search').click()
driver.find_element_by_id('search').send_keys('Saturday Nights')
driver.find_element_by_id('search-icon-legacy').click()
