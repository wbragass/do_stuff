import time
from config import keys
from selenium import webdriver


def disable_user(k):

    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.get(k['office_url'])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="i0116"]').send_keys(k['email'])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="aadTileTitle"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="i0118"]').send_keys(k['phrase'])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="idBtn_Back"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="SearchBox16"]').send_keys(k['user_name'])
    driver.find_element_by_xpath('//*[@id="SearchBox16"]').send_keys(u'\ue007')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="viewport"]/div[4]/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div[1]/div/span').click()
    #driver.find_element_by_xpath('//*[contains(text(),"'+k['user_name']+'")]')
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[3]/div[1]/div/div[1]/div[2]/div[2]/div/button[2]/div/i').click()
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div[3]/div[2]/div/div[2]/div[2]/div/label/div/i').click()

    driver.find_element_by_xpath('//*[@id="id__1357"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('')
    time.sleep(1)
    driver.find_element_by_xpath('')
    time.sleep(1)
    driver.find_element_by_xpath('')
    time.sleep(1)
    driver.find_element_by_xpath('')
    time.sleep(1)
    driver.find_element_by_xpath('')
    time.sleep(1)
    driver.find_element_by_xpath('')
    time.sleep(1)



if __name__ == '__main__':
    disable_user(keys)