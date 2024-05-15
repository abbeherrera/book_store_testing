# Shop: отображение, скидка товара
# 1. Откройте https://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Откройте книгу "Android Quick Start Guide"
# 5. Добавьте тест, что содержимое старой цены = "₹600.00" # используйте assert
# 6. Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert
# 7. Добавьте явное ожидание и нажмите на обложку книги
# •
# Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
# 8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import selenium.webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

address_mail="https://practice.automationtesting.in"
email="675@mail.ru"
password="eRtyu$hjrykl"

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
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
#li.post-169.product_cat-android.product_tag-android > a.woocommerce-LoopProduct-link
btn_android=driver.find_element_by_css_selector("li.post-169.product_cat-android.product_tag-android > a.woocommerce-LoopProduct-link")
btn_android.click()
lbl_600=driver.find_element_by_css_selector("del > span.woocommerce-Price-amount")
price_600=lbl_600.text
assert "₹600.00" in price_600
#print(price_600+cur)
lbl_450=driver.find_element_by_css_selector("ins > span.woocommerce-Price-amount")
price_450=lbl_450.text
print(price_450)
assert "₹450.00" in price_450
img_btn = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, "div.images > a.woocommerce-main-image.zoom")) )
img_btn.click()
close_btn=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.pp_details > a.pp_close")))
close_btn.click()
