"""

Scenario2 Bulgarian Mozillians

Given a site which includes all users of Mozilla: https://mozillians.org/en-US/
When search for keyword 'bulgaria' in the site
Then the results are all Bulgarian Mozillians

"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def find_bulgarians(driver):
    driver.get("https://mozillians.org/en-US/")
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("bulgaria")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source

find_bulgarians(webdriver.Firefox())


