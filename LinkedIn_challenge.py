from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def  main():
    url =  "https://www.linkedin.com/signup/"
    driver = webdriver.Chrome("./chromedriver")
    driver.get(url)
    username = driver.find_element(By.ID, 'email-address')
    username.send_keys('kalLinkedIn@challenge.com')
    password=driver.find_element(By.ID, 'password')
    password.send_keys('your_password')
    signup_button = driver.find_element(By.CLASS_NAME, 'join-form__form-body-submit-button')
    signup_button.click()
    print("account registered")
    
main()

    

