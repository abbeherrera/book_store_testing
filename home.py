# 1. Откройте https://practice.automationtesting.in/
# 2. Проскролльте страницу вниз на 600 пикселей
# 3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
# 4. Нажмите на вкладку "REVIEWS"
# 5. Поставьте 5 звёзд
# 6. Заполните поле "Review" сообщением: "Nice book!"
# 7. Заполните поле "Name"
# 8. Заполните "Email"
# 9. Нажмите на кнопку "SUBMIT"
#from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import selenium.webdriver

site_address="https://practice.automationtesting.in"
email="123@mail.ru"
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(site_address)
driver.execute_script("window.scrollBy(0, 600);")
#text-22-sub_row_1-0-2-0-0 > div > ul > li > a.woocommerce-LoopProduct-link
btn_ruby=driver.find_element_by_css_selector(" li.product_cat-selenium>a.woocommerce-LoopProduct-link")
btn_ruby.click()
btn_review=driver.find_element_by_css_selector("li.reviews_tab > a")
btn_review.click()
btn_5stars=driver.find_element_by_css_selector("a.star-5")
btn_5stars.click()
tfld_review=driver.find_element_by_id("comment")
tfld_review.send_keys("Nice book!")
tfld_name=driver.find_element_by_id("author")
tfld_name.send_keys("Vlad")
tfld_email=driver.find_element_by_id("email")
tfld_email.send_keys(email)
btn_submit=driver.find_element_by_id("submit")
btn_submit.click()


