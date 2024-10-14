import time
from selenium.webdriver.common.by import By


def test_add_to_cart_button_is_displayed(browser):
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Ожидаем несколько секунд, чтобы убедиться, что страница загружена
    time.sleep(30)

    # Проверяем наличие кнопки добавления в корзину
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert button, "Add to cart button is not displayed"