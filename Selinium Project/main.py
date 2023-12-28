import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = 'C:/chrome-Development/chromedriver-win64/chromedriver.exe'

service = webdriver.ChromeService(executable_path=chrome_driver_path)
service.start()
driver = webdriver.Chrome()

# driver.get("https://www.amazon.com/HP-15-6-Laptop-Micro-Edge-Quad-Core/dp/B0BTBJT84C/ref=sr_1_1_sspa?crid=1643NDWPB4VEP&keywords=laptop%2Bhp%2Bi5&qid=1700901108&s=pc&sprefix=laptop%2Bhp%2Ccomputers%2C585&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")
# price_tag = driver.find_element(By.CSS_SELECTOR, value="span.apexPriceToPay")
# print(price_tag.text)

#
driver.get("https://www.python.org/")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# sometimes, it's extremely hard to even find an element even by CCC_SELECTOR, then
# if all else fails, one that will always work is "the XPATH"
# The XPATH  is a way of locating a specific HTML element by a path structure

# submit_bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(submit_bug_link.text, submit_bug_link.get_attribute("href"))

# challenge
event_list = {}
# events_tag = driver.find_element(By.CLASS_NAME, "event-widget")
# event_date = events_tag.find_element(By.CLASS_NAME, "say-no-more")
# event_title = events_tag.find_element(By.CSS_SELECTOR, ".menu li a")
#, print(event_date.text, event_title.text)

events_tags = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul li")
print(events_tags)
i = 0
for event_tag in events_tags:
    event_date = event_tag.find_element(By.TAG_NAME, "time").text
    event_title = event_tag.find_element(By.TAG_NAME, "a").text
    new_event = {
        i:
        {
            "time": event_date,
            "name": event_title
        }
    }
    event_list.update(new_event)
    i += 1
    print(new_event)

print(event_list)


# Another way
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)


time.sleep(69)
driver.quit()
