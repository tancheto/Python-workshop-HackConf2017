"""
Scenario1 Opencart Featured Products

Given a site online shop: http://shop.pragmatic.bg/index.php?route=common/home
And Featured products on the Home page
When visit the site
And define a function featured_products(driver) where driver is a Selenium driver object
Then return name and price of all the featured products
And close the site

"""

from selenium import webdriver

def featured_products(driver):
    lst = []
    driver.get("http://shop.pragmatic.bg/index.php?route=common/home")
    products = driver.find_elements_by_class_name('box-product')

    print(len(products))

    for i in products:
        name = i.find_element_by_xpath(".//div[@class='name']").text
        price = i.find_element_by_xpath(".//div[@class='price']").text

        lst.append((name, price))

    return lst


print(featured_products(webdriver.Firefox()))
