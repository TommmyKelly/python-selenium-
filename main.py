from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

opt = Options()
opt.headless = True
chrome_driver_path = r'C:\Users\User\AppData\Local\SeleniumBasic\chromedriver.exe'
ser = Service(chrome_driver_path)

driver = webdriver.Chrome(service=ser,)
# driver = webdriver.Chrome(service=ser, options=opt)  # open headless
driver.get('http://secure-retreat-92358.herokuapp.com/')


first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
first_name.send_keys('Tommy')
last_name.send_keys('Kelly')
email.send_keys('tommy_kelly@icloud.com')

email.send_keys(Keys.ENTER)

#driver.find_element(By.CSS_SELECTOR, '.form-signin button').click()
