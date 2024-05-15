# Shop: количество товаров в категории
# 1. Откройте https://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Откройте категорию "HTML"
# 5. Добавьте тест, что отображается три товара
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
btn_login=driver.find_element_by_css_selector("p:nth-child(3) > input.woocommerce-Button.button")
btn_login.click()
tab_shop=driver.find_element_by_link_text("Shop")
tab_shop.click()
#woocommerce_product_categories-2 > ul > li.cat-item.cat-item-19 > a
btn_html=driver.find_element_by_css_selector("#woocommerce_product_categories-2 > ul > li.cat-item.cat-item-19 > a")
btn_html.click()
items=driver.find_elements_by_css_selector("a.woocommerce-LoopProduct-link")
#.purchasable.product-type-simple > a.woocommerce-LoopProduct-link
print("Отображается  товаров: ",len(items))