from pyotp import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://accounts.google.com/signin")
wait = WebDriverWait(driver,10)
# enter the email
email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
email.send_keys("2fatest2fa@gmail.com")


nextButton = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Next']")))
nextButton.click()
# time.sleep(1)

# nextButton.send_keys(u'\ue007') #unicode for enter key
# time.sleep(2)

# enter password
password = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
password.send_keys("password goes here")


nextButton = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Next']")))
nextButton.click()
time.sleep(1)

# click on signin button
driver.find_element_by_xpath("//input[@id='signInSubmit']").click()

#wait for the 2FA feild to display
authField = wait.until(EC.presence_of_element_located((By.xpath, "xpath goes here")))
# get the token from google authenticator
totp = TOTP("secret goes here")
token = totp.now()
print (token)
# enter the token in the UI
authField.send_keys(token)
# click on the button to complete 2FA
driver.find_element_by_xpath("xpath of the button goes here").click()
# now open new tab
driver.execute_script("""window.open("https://sellercentral.amazon.de/listing/download?ref=ag_dnldinv_apvu_newapvu")""")
# continue with your logic from here



#navigate to gmail
driver.get("https://mail.google.com/")

