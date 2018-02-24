from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def get_weather(driver, days):

    if days<1 or days>10:
        return None

    else:
        lst=[]
        driver.get("http://www.bbc.com/weather/727011")
        time.sleep(10)
        daytabs = driver.find_elements_by_class_name("daily__day-tab")

        for index in range(days):

            if index == 0:
                maxtemp = driver.find_element_by_css_selector("td.max-temp").text
            else:
                maxtemp = daytabs[index].find_element_by_class_name("units-value").text

            weathertype = daytabs[index].find_element_by_class_name("weather-type-image").get_attribute("title")

            #name= daytabs[index].find_element_by_class_name("day-name").get_attribute("aria-label")
            lst.append((weathertype, maxtemp))

        return lst

print(get_weather(webdriver.Firefox(),10))














