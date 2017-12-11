from  selenium import webdriver
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver=webdriver.Firefox()
wait=WebDriverWait(driver,300)
driver.get('https://hib.iiit-bh.ac.in/Hibiscus/Login/?client=iiit')
captcha=driver.find_element_by_id('txtCaptcha')
ans=captcha.get_attribute('value')
#print(ans)
userid='your id'  #your roll no
userpwd='your password' #your password
usrnm=driver.find_element_by_name('uid')
pwd=driver.find_element_by_name('pwd')
usrnm.send_keys(userid)
pwd.send_keys(userpwd)
captcha=driver.find_element_by_id('txtInput')
captcha.send_keys(ans)
submit=driver.find_element_by_name('sub')
submit.click()
driver.get("https://hib.iiit-bh.ac.in/Hibiscus/Start/aisMenu.php")
mycourse=wait.until(EC.presence_of_element_located((By.LINK_TEXT,'My Course (s)')))
mycourse.click()
courselist = driver.find_elements_by_xpath("//a[@href]") #to get all elemnts with href tag links in a course page
for course in range(1,10): #here 10 refers to total 9 subjects if you have more subjects increase its value
    courselist = driver.find_elements_by_xpath("//a[@href]")  # to get all elemnts with href tag links in a course page
    courselist[course].click()
    courseoption=driver.find_elements_by_xpath("//a[@href]")
    courseoption[15].click() #for feedback option
    teacher=driver.find_elements_by_xpath("//a[@href]")  #list of teachers
    teacher[0].click()
    for i in range(1,14):
        option=driver.find_elements_by_name(i)
        option[3].click()   #option 3 is to select 'Good' u can change it to select other options
    option=driver.find_element_by_name('14')
    option.clear()
    option.send_keys('null')   #null is written in the text boxes u can change it to type whatever you want to
    for i in range(48,50):
        option=driver.find_element_by_name(i)
        option.clear()
        option.send_keys('null')   #null is written in the text boxes u can change it to type whatever you want to
    option=driver.find_element_by_name('49')
    submit=option.send_keys(Keys.TAB+Keys.RETURN)
    time.sleep(2)
    for i in range(4):
        driver.back()
time.sleep(5)
driver.close()