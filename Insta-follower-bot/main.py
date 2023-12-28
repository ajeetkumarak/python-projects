
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

INSTA_USERNAME = "i_msaam"
INSTA_PASSWORD = "7Jw!tzn@AOMB$0uA4%g"
KNOWN_USER = "billionaires.tip"


class InstaBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login_insta(self):
        self.driver.get(url="https://www.instagram.com/")
        time.sleep(11)
        username_box = self.driver.find_element(By.NAME, "username")
        password_box = self.driver.find_element(By.NAME, "password")

        username_box.send_keys(INSTA_USERNAME)
        password_box.send_keys(INSTA_PASSWORD)
        time.sleep(3)
        password_box.send_keys(Keys.ENTER)
        time.sleep(15)
        save_info_button = self.driver.find_element(By.TAG_NAME, "button")
        save_info_button.click()
        time.sleep(39)
        not_now_xpath = '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'
        notification_on_button = self.driver.find_element(By.XPATH, not_now_xpath)
        notification_on_button.click()
        print(notification_on_button)
        time.sleep(36)
        
    def find_followers(self):
        time.sleep(9)
        self.driver.get(url=f"https://www.instagram.com/{KNOWN_USER}/followers/")
        time.sleep(31)

        # followers_popup = self.driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        followers_popup = self.driver.find_element(By.CSS_SELECTOR, '._aano')
        print(followers_popup.text)
        time.sleep(111)
        follow_button = self.driver.find_elements(By.XPATH, "//*[text()='Follow']")
        for button in follow_button:
            print(button.text)
            button.click()
            time.sleep(9)
            self.driver.execute_script("arguments[1].scrollTop = arguments[1].scrollHeight", followers_popup)

        time.sleep(999)


bot = InstaBot()
bot.login_insta()
# bot.search_user(KNOWN_USER)
bot.find_followers()
