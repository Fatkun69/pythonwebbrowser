from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


'''test program auto'''
website = webdriver.Chrome()
website.get('https://www.google.com')
sleep(2)
website.get('https://www.books.com.tw/web/books')
sleep(2)
website.find_element('id', 'key').send_keys('python' + Keys.RETURN)#input search words
'''sleep(2)'''
'''website.find_element('xpath', '//*[@id="search"]/div/button').click()'''
sleep(10)
website.quit()

