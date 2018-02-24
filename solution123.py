from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_weather(driver,days):
    if int(days)!=days or days>10 or days<1:
        return None
    returnlst=[]
    driver.get("http://www.bbc.com/weather/727011")

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "daily")))
        daytabs=driver.find_elements_by_class_name("daily__day-tab")

        for index in range(days):
            #sometimes it doesnt give max for today
            if index==0:
                maxtemp=driver.find_element_by_css_selector("td.max-temp").text
            else:
                maxtemp=daytabs[index].find_element_by_class_name("units-value").text

            weathertype=daytabs[index].find_element_by_class_name("weather-type-image").get_attribute("title")
            returnlst.append((weathertype,maxtemp))


    finally:
        driver.quit()
        return lst



print (get_weather(webdriver.Firefox(),5))
