# Registration_login: регистрация аккаунта
# 1. Откройте https://practice.automationtesting.in/
# 2. Нажмите на вкладку "My Account"
# 3. В разделе "Register", введите email для регистрации
# 4. В разделе "Register", введите пароль для регистрации
# • составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
# • почту и пароль сохраните, потребуюутся в дальнейшем
# 5. Нажмите на кнопку "Register"
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
tfld_email=driver.find_element_by_id("reg_email")
tfld_email.send_keys(email)
tfld_psswd=driver.find_element_by_id("reg_password")
tfld_psswd.send_keys(password)
btn_register=driver.find_element_by_name("register")
btn_register.click()