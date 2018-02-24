"""
Scenario3  You Tube views

Given the site You Tube: https://www.youtube.com/
When search for a particular video; example: 'Despacito'
Then return the views of that video

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def views(driver,name):
    driver.get("https://www.youtube.com/")

    #elem = driver.find_element_by_id('search').send_keys("blah")

    elem = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "search"))
    )

    #elem.clear()
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source

    content=driver.find_elements_by_id("contents")

    link=content[0].find_element_by_xpath("//div[@class='yt-simple-endpoint']").get_attribute('href')

    driver.get("%s" %link)
    view= driver.find_element_by_class_name("view-count")

    return view

print(views(webdriver.Firefox(),"despacito"))

