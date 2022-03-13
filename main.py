from selenium import webdriver
import time
EMAIL = "koshtiakanksha12@gmail.com"
PASSWORD = "12M@y2001"
URL = "https://www.linkedin.com/jobs/search/?f_AL=true&f_JT=I&f_WT=2&geoId=102713980&keywords=python%20developer&location=India"

chrome_driver_path = r"C:\Users\kosht\OneDrive\Desktop\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)
time.sleep(10)
sign_in_button = driver.find_element_by_xpath("/html/body/div[3]/a[1]")
sign_in_button.click()
time.sleep(5)
email = driver.find_element_by_id("username")
email.send_keys(EMAIL)
password = driver.find_element_by_id("password")
password.send_keys(PASSWORD)
driver.find_element_by_xpath("//*[@id='organic-div']/form/div[3]/button").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[3]/div[2]/div/section[2]/div"
                             "/div/div[1]/div/div[1]/div/div[2]/div[3]/div/div/div/button").click()
time.sleep(2)
phone = driver.find_element_by_class_name("fb-single-line-text__input")
phone.send_keys("8766712080")
driver.find_element_by_css_selector("footer button").click()
time.sleep(2)
driver.close()
