from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


path = "Z:\chromedriver"
driver = webdriver.Chrome(path)
driver.get("https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=1c73a1d7-ced3-492c-8ccf-7a888c222631&client-request-id=fa40f130-9050-4a4e-a2c5-3f29eb2dbdcb&x-client-SKU=Js&x-client-Ver=1.0.9&nonce=a7001a17-f3f3-4f7c-a69e-5f76b508aa81&domain_hint=&sso_reload=true")
print(driver.title)





search = driver.find_element_by_id("i0116")
search.send_keys("teams_username")
search.send_keys(Keys.RETURN)

search_2 = driver.find_element_by_id("i0118")
search_2.send_keys("teams_password")
search.send_keys(Keys.RETURN)

time.sleep(4)

driver.find_element_by_xpath('//input[@class="button ext-button primary ext-primary"]').click()

time.sleep(4)
driver.find_element_by_id('idSIButton9').click()


time.sleep(40)
driver.find_element_by_xpath('//*[@id="personDropdown"]/div/div/div/profile-picture/img').click()

time.sleep(3)
driver.find_element_by_xpath('//*[@id="settings-dropdown-list"]/li[1]/div/div[2]/button').click()

time.sleep(3)
upload = driver.find_element_by_xpath('//*[@id="changeUserInfo-uploadBtn"]/div/div[2]').click()


time.sleep(10)
driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div/div/div/div[3]/div/div[2]/button').click()

time.sleep(3)
driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div/div/div/div[3]/div/div[1]/button').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="personDropdown"]/div/div/div/profile-picture/img').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="logout-button"]').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="tilesHolder"]/div/div/div').click()














