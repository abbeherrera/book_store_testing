# Registration_login: логин в систему
# 1. Откройте https://practice.automationtesting.in/
# 2. Нажмите на вкладку "My Account"
# 3. В разделе "Login", введите email для логина # данные можно взять из предыдущего теста
# 4. В разделе "Login", введите пароль для логина # данные можно взять из предыдущего теста
# 5. Нажмите на кнопку "Login"
# 6. Добавьте проверку, что на странице есть элемент "Logout"
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import selenium.webdriver

address_mail="https://practice.automationtesting.in"
email="675@mail.ru"
password="eRtyu$hjrykl"

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(address_mail)
tab_myaccount=driver.find_element_by_link_text("My Account")
tab_myaccount.click()
#eRtyu$%hjry
tfld_email=driver.find_element_by_id("username")
tfld_email.send_keys(email)
tfld_psswd=driver.find_element_by_id("password")
tfld_psswd.send_keys(password)
btn_login=driver.find_element_by_css_selector(" p:nth-child(3) > input.woocommerce-Button.button")
btn_login.click()
#Logout
items_logout=driver.find_elements_by_link_text("Logout")
count=len(items_logout)
if count==0:
    print("is not found elements Logout")
else:
    print(count,"element(s) \"Logout\"")
    