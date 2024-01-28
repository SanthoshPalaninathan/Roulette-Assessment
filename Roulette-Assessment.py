from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service()
driver = webdriver.Chrome(options=options,service=service_obj)
driver.get("https://csgoempire.com/roulette")
driver.maximize_window()

#Entering the bet value maually
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("1.00")

#Clicking bet 100
driver.find_element(By.CSS_SELECTOR, "div[class='bet-input__controls'] button:nth-child(1)").click()

#Clicking the sound option to off
driver.find_element(By.XPATH, "//span[contains(text(),'Sound on')]").click()

#Clicking in Chat option
driver.find_element(By.CLASS_NAME, "flex").click()

#Fetching and printing the Roulette race message
message = driver.find_element(By.XPATH, "//div[@class='mb-2 w-auto break-words text-light-grey-1 md:mb-0']").text
print(message)

#Fetching and printing the CSGO Empire info
message1 = driver.find_element(By.XPATH, "//p[@class='size-small mb-md text-xs']").text
print(message1)

#Verifying the the CSGO Empire info is correct or not by assert option
assert "CSGOEmpire" in message1

#Printing the site name
print(driver.title)

#Printing the URL
print(driver.current_url)


