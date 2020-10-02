import pytest
from selenium import webdriver
from pageobject.LoginPage import LoginPage

class LoginPage_test:
    baseUrl="https://admin-demo.nopcommerce.com/"
    userName="admin@yourstore.com"
    userPassword="admin"

    def homePageTitle_test(self,setUp):
        self.driver=setUp
        self.driver.get(self.baseUrl)
        actualTitle=self.driver.title
        self.driver.close()
        if actualTitle=="Your store. Login":
            assert True
        else:
            self.driver.save_screenshot("\\.Screeshots\\"+"homePageTitle_test.png")
            assert False

    def user_Login_test(self,setUp):
        self.driver = setUp
        self.driver.get(self.baseUrl)
        self.log=LoginPage(self.driver)
        self.log.setUserName(self.username)
        self.log.setPassword(self.password)
        self.log.clickLogin()
        actualTitle=self.driver.title
        if actualTitle=="Dashboard / nopCommerce administration":
            assert True
        else:
            self.driver.save_screenshot("\\.Screeshots\\"+"homePageTitle_test.png")
            assert False
        self.driver.close()










