from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
website= 'https://www.landwatch.com/california-land-for-sale/san-diego-county-region/price-50000-99999/sort-acres-high-low'

driver=webdriver.Firefox(executable_path="C:/Users/james/Downloads/geckodriver-v0.31.0-win64/geckodriver.exe")
driver.get(website)
prices=driver.find_elements_by_class_name("b04f6")
title=driver.find_elements_by_css_selector("span[title]")
prices_list = []
info_list=[]

for p in prices:
    #print(p.text)
    prices_list.append(p.text)

#print(prices_list)

for t in title:
    #print(t.text)
    info_list.append(t.text)
#print(info_list)
prices_dict = dict(zip(prices_list, info_list))
#print(prices_dict)

for key in prices_dict:
    if key < "$75,000":
        print("Price : {}, Info:{}".format(key, prices_dict[key]))
    

driver.close()

