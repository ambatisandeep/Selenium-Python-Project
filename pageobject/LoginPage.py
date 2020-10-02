from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    user_EmailId_id="Email"
    user_Password_id="Password"
    submit_LoginButton_xpath="//*[@type='submit']"

    def def__init__(self, driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.id,self.user_EmailId_id).clear()
        self.driver.find_element(By.id,self.user_EmailId_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.id, self.user_Password_id).clear()
        self.driver.find_element(By.id, self.user_Password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.submit_LoginButton_xpath)
        







