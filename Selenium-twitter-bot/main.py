from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Chrome()

# driver.get(url="https://www.speedtest.net/")
# 
# 
# go_button = driver.find_element(by=By.CSS_SELECTOR, value='.start-button a .start-text')
# # go_button = driver.find_element(by=By.CSS_SELECTOR, value='.js-start-test')
# time.sleep(11)
# go_button.click()
# 
# time.sleep(61)
# 
# result_id = driver.find_element(By.CSS_SELECTOR, ".result-data a").text
#
# print(result_id)
# 
# download_data = driver.find_element(By.CSS_SELECTOR, ".result-item-download .result-data .download-speed")
# print(download_data)
# 
# 
# upload_data = driver.find_element(By.CSS_SELECTOR, ".result-item-upload .result-data .upload-speed")
# print(upload_data)

# -------------------------


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.download_speed = 0
        self.upload_speed = 0

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")

        accept_btn = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        time.sleep(11)
        accept_btn.click()
        time.sleep(11)
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a .start-text")
        print(go_button.text)
        go_button.click()
        time.sleep(191)
        self.download_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.upload_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
print(f"Down: {bot.download_speed} MB/s")
print(f"Up: {bot.upload_speed} MB/s")

time.sleep(119)







































# driver.quit()
