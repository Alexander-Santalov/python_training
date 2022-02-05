from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ProjectHelperButtons:
    def __init__(self, app):
        self.app = app

    #  Клик по кнопке по CSS локатору
    def button_click(self, button_locator):
        try:
            wd = self.app.wd
            WebDriverWait(wd, 5).until(
              EC.element_to_be_clickable((By.CSS_SELECTOR, "%s" % button_locator)))
            wd.find_element(By.CSS_SELECTOR, "%s" % button_locator).click()
        except Exception as e:
            assert e == TimeoutException, f"Кнопка  {button_locator} не кликабельна"

    #  Проверка, что кнопка кликабельна
    def assert_button_on(self, button_locator):
        wd = self.app.wd
        btn = WebDriverWait(wd, 5).until(
          EC.element_to_be_clickable((By.CSS_SELECTOR, "%s" % button_locator)))
        assert btn.get_attribute(
          "disabled") != 'true', f"Ожидаемый результат = {None}, Фактический = {btn.get_attribute('disabled')}"

    #  Проверка, что кнопка не кликабельна
    def assert_button_off(self, button_locator):
        wd = self.app.wd
        btn = WebDriverWait(wd, 5).until(
          EC.visibility_of_element_located((By.CSS_SELECTOR, "%s" % button_locator)))
        assert btn.get_attribute(
          "disabled") == 'true', f"Ожидаемый результат = {'true'}, Фактический = {btn.get_attribute('disabled')}"

    #  Проверка имени кнопки
    def assert_name_button(self, button_locator, text_button):
        wd = self.app.wd
        WebDriverWait(wd, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "%s" % button_locator)))
        element = wd.find_element(By.CSS_SELECTOR, "%s" % button_locator).text
        assert element == text_button, f"Ожидаемый результат = {text_button}, Фактический = {element}"

    #  Возврат свойства кнопки
    def state_button(self, button_locator, atribut):
        wd = self.app.wd
        btn = WebDriverWait(wd, 5).until(
          EC.visibility_of_element_located((By.CSS_SELECTOR, "%s" % button_locator)))
        return btn.get_attribute(atribut)
