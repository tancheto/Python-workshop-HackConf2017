def f_c(x):
    """returns the constant 4 for any input parameter"""
    return 4

#print (f_c(10))

def f_x(x, a, b):
    return a*x + b

#print(f_x(1,2,3))

def sum(x):
    return f_x(x, 1, 1)+f_x(x, 2, 2)+f_x(x, 3, 3)

#print(sum(10))

def num_add(a, b):
    return a+b

def num_sub(a, b):
    return a-b

def num_mul(a, b):
    return a*b

def num_div(a, b):
    return a/b

def num_floor(a, b):
    return a//b

def num_rem(a, b):
    return a%b

IS_TRUE=True

IS_FALSE=False

PANCAKE_INGREDIENTS = {'flour': 2,
                       'eggs': 4,
                       'milk': 200,
                       'butter': IS_FALSE,
                       'salt': 0.001
                       }

def ingredient_exists(ingr, dict):
    return ingr in dict

def fatten_pancakes(dict):
    ingr=dict.copy()
    ingr['eggs']=6
    ingr['butter']=True
    return ingr

def add_sugar(dict):
    ingr=dict.copy()
    ingr['sugar'] = True
    return ingr

def remove_salt(dict):
    ingr=dict.copy()
    del ingr['salt']
    return ingr

FIBONACCI_NUMBERS=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

def add_fibonacci(lst):
    lst.append(lst[-1]+lst[-2])
    return lst

def fib_exists(lst, n):
    return n in lst

def which_fib(lst, n):
    return lst.index(n)+1
#----------------------------#
def sum_of_digits(n):
    if n < 0:
        n = -n
    sum = 0
    while n != 0:
        x = n % 10
        sum = sum + x
        n = n // 10
    return sum

def to_digits(n):
    lst = []
    while n != 0:
        x = n % 10
        lst.insert(0, x)
        n = n // 10
    return lst

def to_number(digits):
    index = 0
    x = 0
    while digits!=[]:
        x = x + (10 ** index) * digits[-1]
        del digits[-1]
        index = index + 1
    return x

def count_vowels(str):
    num=0

    for i in str:
        if i in 'aAeEiIoOuUyY':
            num=num+1
    return num

def count_consonants(str):
    num = 0

    for i in str:
        if i in 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ':
            num = num + 1
    return num

def prime_number(number):
    import math
    if number == 1:
        return False
    x = 2
    while x <= math.sqrt(number):
        if number % x == 0:
            return False
        x = x + 1
    return True

def faktoriel(n):
    x=1
    fakt=1
    while x<=n:
        fakt=fakt*x
        x=x+1
    return fakt

def fact_digits(n):
    suma=0
    while n>0:
        x=n%10
        suma=suma+faktoriel(x)
        n=n//10
    return suma

def add_fibonacci(lst):
    lst.append(lst[-1]+lst[-2])
    return lst

def fibonacci(n):
    li=[]
    x=1
    for x in range(n):
        if(x==1 and x==2):
            li.append(1)
        if(x>2):
            add_fibonacci(li)
        x=x+1
    return li

def fib_number(n):
    li=fibonacci(n)
    s= map(str,li)
    s=''.join(s)
    s=int(s)
    return s

def palindrome(obj):
    obj=str(obj)
    length=len(obj)
    x=0
    while x<length/2:
        if obj[x]!=obj[-1-x]:
            return False
        x+=1
    return True


def char_histogram(string):
    di={}

    while(string!=""):
        x=string[0]
        flag=0
        for y in string:
            if x==y:
                flag += 1
            di.update({x: flag})
            string = string.replace(x, "")
    return di


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_weather(driver, days):

    if days<1 or days>10:
        return None

    else:
        lst=[]
        driver.get("http://www.bbc.com/weather/727011")
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

