from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.flipkart.com/"

driver = webdriver.Chrome(executable_path="C:\\Users\\DELL\\Documents\\Downloads\\chromedriver.exe")
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)
print(driver.title)
driver.find_element(By.XPATH,"//*[@class='_2AkmmA _29YdH8']").click()

driver.find_element(By.XPATH,"//*[@class='LM6RPg']").click()
driver.find_element(By.XPATH,"//*[@class='LM6RPg']").send_keys("Phones")
driver.find_element(By.XPATH,"//*[@class='vh79eN']").click()
time.sleep(5)
gb_ele = driver.find_element(By.XPATH,"//div[text()='6 GB & Above']/preceding::div[@class='_1p7h2j']")
gb_ele.click()


time.sleep(5)


driver.quit()
