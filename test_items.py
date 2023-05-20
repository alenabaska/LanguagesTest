import time
from selenium.webdriver.common.by import By

def test_guest_should_see_login_link(browser):
    link =  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket"), "button exist"
    time.sleep(30)

