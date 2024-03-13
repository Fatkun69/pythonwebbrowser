from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

list_number = ['cawd-628', 'kwbd-364', 'sone-071']
list_number.append('fway-001')


'''open browser'''
web = webdriver.Chrome()
web.get('https://www.javdb.com')
sleep(0.1)
web.find_element('xpath', '/html/body/div[1]/div[2]/footer/a[1]').click()
sleep(0.1)



for i in range(len(list_number)):
    web.find_element('id', 'video-search').send_keys(str(list_number[i]) + Keys.RETURN)
    sleep(5)
    '''click in correct picture'''

    test_name = str(list_number[i]).upper()
    print("upper : " + test_name)


    web.find_element('id', 'video-search').clear()

    sleep(0.1)
    '''end for i'''

sleep(5)
web.quit()


'''
1
/html/body/section/div/div[6]/div[1]/a/div[2]/strong
2
/html/body/section/div/div[6]/div[2]/a/div[2]/strong
3
/html/body/section/div/div[6]/div[3]/a/div[2]/strong
4
/html/body/section/div/div[6]/div[4]/a/div[2]/strong

'''