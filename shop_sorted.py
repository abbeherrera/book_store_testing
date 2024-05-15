# Shop: сортировка товаров
# 1. Откройте https://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
# •
# Используйте проверку по value
# 5. Отсортируйте товары по цене от большей к меньшей
# •
# в селекторах используйте класс Select
# 6. Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
# 7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
# •
# Используйте проверку по value
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import selenium.webdriver
from selenium.webdriver.support.select import Select

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
btn_login=driver.find_element_by_css_selector("p:nth-child(3) > input.woocommerce-Button.button")
btn_login.click()
tab_shop=driver.find_element_by_link_text("Shop")
tab_shop.click()
#content > form > select
#selector=driver.find_element_by_css_selector("#content > form > select")
#print(selector.text)
opt_menuorder=driver.find_element_by_css_selector("select > option:nth-child(1)")
print("Default sorting is selected:",opt_menuorder.is_selected())
element=driver.find_element_by_css_selector("#content > form > select")
# #select > option:nth-child(1)
selector=Select(element)
#opt_menuorder=selector.select_by_value("menu_order")
# opt_menuorder.
# print(opt_menuorder.)
selector.select_by_value("price-desc")
# option_
opt_price_desc=driver.find_element_by_css_selector("select > option:nth-child(6)")
print("sorting by price desc  is selected:",opt_price_desc.is_selected())

