# Shop: покупка товара
# 1. Откройте https://practice.automationtesting.in/
# # в этом тесте логиниться не нужно
# 2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
# 3. Добавьте в корзину книгу "HTML5 WebApp Development"
# 4. Перейдите в корзину
# 5. Нажмите "PROCEED TO CHECKOUT"
# •
# Перед нажатием, добавьте явное ожидание
# 6. Заполните все обязательные поля
# • Перед заполнением first name, добавьте явное ожидание
# • Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
# • Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку
# нажмите на неё, затем на вариант в списке ниже
# 7. Выберите способ оплаты "Check Payments"
# •
# Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
# 8. Нажмите PLACE ORDER
# 9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
# 10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import selenium.webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# 1. Откройте https://practice.automationtesting.in/
# # в этом тесте логиниться не нужно
address="https://practice.automationtesting.in"

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get(address)
# 2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
tab_shop=driver.find_element_by_link_text("Shop")
tab_shop.click()
driver.execute_script("window.scrollBy(0, 300);")
# 3. Добавьте в корзину книгу "HTML5 WebApp Development"
btn_html5=driver.find_element_by_css_selector("li.post-182 > a.button.add_to_cart_button.ajax_add_to_cart")
#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart
btn_html5.click()
sleep(5)
# 4. Перейдите в корзину
btn_basket=driver.find_element_by_css_selector("#wpmenucartli > a")
btn_basket.click()
sleep(5)
# 5. Нажмите "PROCEED TO CHECKOUT"
# •
# Перед нажатием, добавьте явное ожидание
btn_checkout=WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a.checkout-button")))
btn_checkout.click()
# div.wc-proceed-to-checkout > a.checkout-button
# 6. Заполните все обязательные поля
# • Перед заполнением first name, добавьте явное ожидание
# • Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
# • Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку
# нажмите на неё, затем на вариант в списке ниже
firstname,lastname,email,phone,country,street,city,post="Jean-Loup","Cretin","123@ya.ru","4566783670","France","Batignoles","Paris","75012"
tfld_Fname=WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,"billing_first_name")))
tfld_Fname.send_keys(firstname)
tfld_Lname=driver.find_element_by_id("billing_last_name")
tfld_Lname.send_keys(lastname)
tfld_email=driver.find_element_by_id("billing_email")
tfld_email.send_keys(email)
tfld_phone=driver.find_element_by_id("billing_phone")
tfld_phone.send_keys(phone)
btn_country=driver.find_element_by_css_selector("#s2id_billing_country > a")
btn_country.click()
tfld_country=driver.find_element_by_css_selector("#s2id_autogen1_search")
tfld_country.send_keys("Fra")
btn_countryfix=driver.find_element_by_css_selector("span.select2-match")
btn_countryfix.click()
#span.select2-match
# li.select2-results-dept-0.select2-result.select2-result-selectable.select2-highlighted
#select2-result-label-5550 > span
#select2-result-label-3364
#s2id_autogen1
tfld_street=driver.find_element_by_id("billing_address_1")
tfld_street.send_keys(street)
tfld_post=driver.find_element_by_id("billing_postcode")
tfld_post.send_keys(post)
tfld_post=driver.find_element_by_id("billing_city")
tfld_post.send_keys(city)
# 7. Выберите способ оплаты "Check Payments"
# •
# Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep

driver.execute_script("window.scrollBy(0, 600);")
sleep(3)
rbtn_chpayment=driver.find_element_by_id("payment_method_cheque")
rbtn_chpayment.click()
# 8. Нажмите PLACE ORDER
btn_order=driver.find_element_by_id("place_order")
btn_order.click()
# 9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
lbl_thanks=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"p.woocommerce-thankyou-order-received")))
assert "Thank you. Your order has been received." in lbl_thanks.text
# p.woocommerce-thankyou-order-received
# 10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
lbl_check=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR," tr:nth-child(3) > td")))
assert "Check Payments" in lbl_check.text


