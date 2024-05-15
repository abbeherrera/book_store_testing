# Shop: отображение страницы товара
# 1. Откройте https://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Откройте книгу "HTML 5 Forms"
# 5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
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
#  li.post-181.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link
# li.post-181.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category> a.woocommerce-LoopProduct-link
# li.post-181.product.type-product.status-publish.product_cat-html> a.woocommerce-LoopProduct-link
# li.post-181.product> a.woocommerce-LoopProduct-link
# li.post-181> a.woocommerce-LoopProduct-link
btn_html5=driver.find_element_by_css_selector("li.post-181> a.woocommerce-LoopProduct-link")
btn_html5.click()
lbl_html5forms=driver.find_element_by_css_selector("#product-181 > div.summary.entry-summary > h1")
print("Label: ",lbl_html5forms.text)