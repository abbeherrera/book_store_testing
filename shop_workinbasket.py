# Shop: работа в корзине
# Иногда, даже явные ожидания не помогают избежать ошибки при нахождении элемента, этот сценарий один из таких, используйте time.sleep()
# 1. Откройте https://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# 2. Нажмите на вкладку "Shop"
# 3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# • Перед добавлением первой книги, проскролльте вниз на 300 пикселей
# • После добавления 1-й книги добавьте sleep
# 4. Перейдите в корзину
# 5. Удалите первую книгу
# •
# Перед удалением добавьте sleep
# 6. Нажмите на Undo (отмена удаления)
# 7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
# •
# Предварительно очистите поле с помощью локатор_поля.clear()
# 8. Нажмите на кнопку "UPDATE BASKET"
# 9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3
# # используйте assert
# 10. Нажмите на кнопку "APPLY COUPON"
# •
# Перед нажатимем добавьте sleep
# 11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
# # если эти книги будут out of stock - тогда вместо них добавьте книгу HTML5 Forms и любую доступную книгу по JS и выполнитетесты по аналогии

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import selenium.webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

address_mail="https://practice.automationtesting.in"
# email="675@mail.ru"
# password="eRtyu$hjrykl"

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(address_mail)
# tab_myaccount=driver.find_element_by_link_text("My Account")
# tab_myaccount.click()
# #eRtyu$%hjry
# tfld_email=driver.find_element_by_id("username")
# tfld_email.send_keys(email)
# tfld_psswd=driver.find_element_by_id("password")
# tfld_psswd.send_keys(password)
# btn_login=driver.find_element_by_css_selector("p:nth-child(3) > input.woocommerce-Button.button")
# btn_login.click()
tab_shop=driver.find_element_by_link_text("Shop")
tab_shop.click()
driver.execute_script("window.scrollBy(0, 300);")
#li.post-182.product-type-simple > a.woocommerce-LoopProduct-link
btn_html5=driver.find_element_by_css_selector("li.post-182 > a.button.add_to_cart_button.ajax_add_to_cart")
#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart
btn_html5.click()
#product-182 > div.summary.entry-summary > form.cart > button
# btn_addhtml5=driver.find_element_by_css_selector("form.cart > button")
# btn_addhtml5.click()
#menu-item-40
# tab_shop1=driver.find_element_by_link_text("Shop")
# tab_shop1.click()
sleep(10)
btn_jsdata=driver.find_element_by_css_selector("li.post-180 >a.button.add_to_cart_button.ajax_add_to_cart")
btn_jsdata.click()
# btn_addjs=driver.find_element_by_css_selector("form.cart > button")
# btn_addjs.click()

btn_basket=driver.find_element_by_css_selector("#wpmenucartli > a")
btn_basket.click()
sleep(20)
# # remove  book 1 
btn_remove1=driver.find_element_by_css_selector("tr:nth-child(1) > td.product-remove > a.remove")
btn_remove1.click()
#tr:nth-child(1) > td.product-remove > a.remove
#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-remove > a
sleep(5)
btn_undo=driver.find_element_by_css_selector("div.woocommerce-message > a")
btn_undo.click()
#page-34 > div > div.woocommerce > div.woocommerce-message > a
#spin
tfld_quant=driver.find_element_by_css_selector("tr:nth-child(1) > td.product-quantity > div.quantity> input.input-text.qty.text")
tfld_quant.clear()
tfld_quant.send_keys("3")
btn_update=driver.find_element_by_css_selector(" tr:nth-child(3) > td > input.button")
btn_update.click()
sleep(5)
lbl_quant=driver.find_element_by_css_selector(" tr:nth-child(1) > td.product-quantity > div > input")
quant_value=lbl_quant.get_attribute("value")
#print("must be 3...",quant_value,type(quant_value))
sleep(3)
assert  int(quant_value)==3 
sleep(3)
btn_coupon=driver.find_element_by_css_selector("div.coupon > input.button")
btn_coupon.click()
#lbl_coupon=driver.find_element_by_link_text("Please enter a coupon code.")
lbl_coupon=driver.find_element_by_css_selector("ul.woocommerce-error> li")
coupon_text=lbl_coupon.text
#print("coupon",coupon_text)
assert "Please enter a coupon code." in  coupon_text


