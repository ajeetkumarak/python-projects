import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# driver.get(url="https://en.wikipedia.org/wiki/Main_Page")
# 
# article_count = driver.find_element(By.ID, "articlecount")
# num_of_articles = article_count.find_element(By.TAG_NAME, "a")
# print(article_count, num_of_articles)
# print(num_of_articles.text)
# 
# # num_of_articles.click()
# 
# 
# content_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# # content_portals.click()
# 
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# ------------------------------------------------------------
driver.get(url="https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

first_name.send_keys("Ajeet")
last_name.send_keys("Kumar")
email.send_keys("jeetak987@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()
time.sleep(46)
driver.quit()