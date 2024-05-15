# Shop: проверка цены в корзине
# 1. Откройте https://practice.automationtesting.in/
# # в этом тесте логиниться не нужно
# 2. Нажмите на вкладку "Shop"
# 3. Добавьте в корзину книгу "HTML5 WebApp Development" # см. комментарии в самом низу
# 4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
# •
# Используйте для проверки assert
# 5. Перейдите в корзину
# 6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
# 7. Используя явное ожидание, проверьте что в Total отобразилась стоимость
# # если эта книга будет out of stock - тогда вместо неё добавьте книгу HTML5 Forms и выполните тесты по аналогии
# # если все книги будут out of stock - тогда пропустите это и следующие два задания

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
driver.implicitly_wait(5)
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
#li.post-169.product_cat-android.product_tag-android > a.woocommerce-LoopProduct-link
#li.post-182.product.product-type-simple > a.woocommerce-LoopProduct-link
#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link
btn_html5webapp=driver.find_element_by_css_selector("li.post-182.product.product-type-simple > a.woocommerce-LoopProduct-link")
btn_html5webapp.click()
#product-182 > div.summary.entry-summary > form > button
btn_addbasket=driver.find_element_by_css_selector( "button.single_add_to_cart_button")
btn_addbasket.click()
lbl_basket_items=driver.find_element_by_css_selector("span.cartcontents")
#li.wpmenucartli > a.wpmenucart-contents > span.cartcontents

lbl_basket_price=driver.find_element_by_css_selector("a.wpmenucart-contents>span.amount")
#li.wpmenucartli > a.wpmenucart-contents > span.cartcontents
basket_item_text=lbl_basket_items.text
basket_price_text=lbl_basket_price.text
print(basket_item_text, basket_price_text)
assert "1" in basket_item_text
assert "₹180.00" in basket_price_text


btn_viewbasket=driver.find_element_by_css_selector( "a.button.wc-forward")
btn_viewbasket.click()

lbl_subTotal=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"tr.cart-subtotal > td > span.woocommerce-Price-amount")))
#page-34 > div > div.woocommerce > div > div > table > tbody > tr.order-total > td > strong > span
price_subTotal=lbl_subTotal.text
print("Subtotal: ",price_subTotal)
lbl_Total=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"strong> span.woocommerce-Price-amount.amount")))
#page-34 > div > div.woocommerce > div > div > table > tbody > tr.order-total > td > strong > span
price_Total=lbl_Total.text
print("Total: ",price_Total)
