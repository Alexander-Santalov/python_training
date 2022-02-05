from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



class ElementsHelper:
    def __init__(self, app):
        self.app = app

    #  Выбор из выпадающего списка по CSS локатору
    def select_dropdown_list(self, field_locator, mode):
        wd = self.app.wd
        WebDriverWait(wd, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "%s" % field_locator)))
        Select(wd.find_element(By.CSS_SELECTOR, "%s" % field_locator)).select_by_value("%s" % mode)

    #  Ввод значения в текстовое поле по CSS локатору
    def field_enter(self, field_locator, testdata):
        wd = self.app.wd
        WebDriverWait(wd, 5).until(
          EC.element_to_be_clickable((By.CSS_SELECTOR, "%s" % field_locator)))
        wd.find_element(By.CSS_SELECTOR, "%s" % field_locator).click()
        wd.find_element(By.CSS_SELECTOR, "%s" % field_locator).clear()
        wd.find_element(By.CSS_SELECTOR, "%s" % field_locator).send_keys("%s" % testdata)

    #  Проверка введенного значения в текстовое поле по CSS локатору
    def assert_field(self, field_locator, testdata):
        try:
            wd = self.app.wd
            field_value = WebDriverWait(wd, 5).until(
              EC.element_to_be_clickable((By.CSS_SELECTOR, "%s" % field_locator)))
            assert field_value.get_attribute(
              "value") == testdata, f"Ожидаемый результат = {testdata}, " \
                                    f"Фактический = {field_value.get_attribute('value')}"
        except Exception as e:
            assert e == TimeoutException, f"Ожидаемый результат = {testdata} не получен по локатору {field_locator}"

    #  Сравнение исходного значения поля с текущим
    def assert_field_state(self, field_locator1, field_locator2):
        wd = self.app.wd
        field_value_start = WebDriverWait(wd, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "%s" % field_locator1)))
        field_value_actual = WebDriverWait(wd, 5).until(
          EC.visibility_of_element_located((By.CSS_SELECTOR, "%s" % field_locator2)))
        field_value_start = field_value_start.get_attribute("value")
        field_value_actual = field_value_actual.get_attribute("value")
        assert field_value_start == field_value_actual, f"Ожидаемый результат = {field_value_start}, Фактический = {field_value_actual}"

    # Проверка всплывающей подсказки об ошибке
    def assert_field_error_on(self, error_locator):
        wd = self.app.wd
        WebDriverWait(wd, 5).until(
          EC.element_to_be_clickable((By.CSS_SELECTOR, "%s" % error_locator)))
        error = len(wd.find_elements(By.CSS_SELECTOR, "%s" % error_locator))
        assert error > 0, f"Ожидаемый результат = {0}, Фактический = {1}"

    # Проверка текста всплывающей подсказки об ошибке
    def assert_field_error_text(self, error_locator, text):
        wd = self.app.wd
        element = WebDriverWait(wd, 5).until(
          EC.element_to_be_clickable((By.CSS_SELECTOR, error_locator)))
        assert element.text == text, f"Ожидаемый результат = {text}, Фактический = {element.text}"

    #  Проверка текста уведомления при сохранении
    def assert_text_notification(self, css_locator, validtext):
        wd = self.app.wd
        element = WebDriverWait(wd, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_locator)))
        assert element.text == validtext, f"Ожидаемый результат = {validtext}, Фактический = {element.text}"
        WebDriverWait(wd, 3).until(EC.staleness_of(element))

    #  Проверка факта появления уведомления при сохранении
    def assert_notification(self, css_locator):
        wd = self.app.wd
        spisok = len(wd.find_elements(By.CSS_SELECTOR, css_locator))
        assert spisok > 0, f"Уведомление после записи не появилось"

    #  Проверка имени поля
    def assert_field_name(self, css_locator, namefield):
        wd = self.app.wd
        WebDriverWait(wd, 5).until(
          EC.visibility_of_element_located((By.CSS_SELECTOR, "%s" % css_locator)))
        element = wd.find_element(By.CSS_SELECTOR, "%s" % css_locator).text
        assert element == namefield, f"Ожидаемый результат = {namefield}, Фактический = {element}"

    #  Проверка имени поля по xpath
    def assert_field_name_xpath(self, css_locator, namefield):
        wd = self.app.wd
        WebDriverWait(wd, 5).until(
            EC.visibility_of_element_located((By.XPATH, "%s" % css_locator)))
        element = wd.find_element(By.XPATH, "%s" % css_locator).text
        assert element == namefield, f"Ожидаемый результат = {namefield}, Фактический = {element}"

    #  Проверка значения элемента по факту его видимости
    def assert_element(self, field_locator, testdata):
        wd = self.app.wd
        field_value = WebDriverWait(wd, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "%s" % field_locator)))
        assert field_value.get_attribute(
            "value") == testdata, f"Ожидаемый результат = {testdata}, Фактический = {field_value.get_attribute('value')}"

    def assert_element_xpath(self, field_locator, testdata):
        wd = self.app.wd
        field_value = WebDriverWait(wd, 5).until(
            EC.visibility_of_element_located((By.XPATH, "%s" % field_locator)))
        assert field_value.get_attribute(
            "value") == testdata, f"Ожидаемый результат = {testdata}, Фактический = {field_value.get_attribute('value')}"


    #  Проверка на сравнение полученного списка с заданным значением
    def assert_list(self, field_locator, testdata):
        wd = self.app.wd
        WebDriverWait(wd, 5).until(
          EC.element_to_be_clickable((By.CSS_SELECTOR, "%s" % field_locator)))
        x = len(wd.find_elements(By.CSS_SELECTOR, "%s" % field_locator))
        assert x == testdata, f"Ожидаемый результат = {testdata}, Фактический = {x}"

    #  Проверка поля на сравнение указанного параметра и заданного значения
    def assert_field_param(self, field_locator, param, testdata):
        wd = self.app.wd
        field_value = WebDriverWait(wd, 5).until(
          EC.visibility_of_element_located((By.CSS_SELECTOR, "%s" % field_locator)))
        assert field_value.get_attribute(
          param) == testdata, f"Ожидаемый результат = {testdata}, Фактический = {field_value.get_attribute(param)}"

    #  Сравнение значения элемента списка с заданным значением
    def assert_element_list(self, field_locator, testdata):
        wd = self.app.wd
        WebDriverWait(wd, 5).until(
          EC.element_to_be_clickable((By.CSS_SELECTOR, "%s" % field_locator)))
        element = wd.find_element(By.CSS_SELECTOR, "%s" % field_locator).text
        assert element == testdata, f"Ожидаемый результат = {testdata}, Фактический = {element}"

    #  Переключение тумблера
    def switch_selector(self, switch_locator_click, switch_locator_value, mode):
        wd = self.app.wd
        WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, switch_locator_click)))
        if mode == "ON":
            switch_on = wd.find_element(By.CSS_SELECTOR, switch_locator_value).is_selected()
            if switch_on is False:
                wd.find_element(By.CSS_SELECTOR, switch_locator_click).click()
        elif mode == "OFF":
            switch_off = wd.find_element(By.CSS_SELECTOR, switch_locator_value).is_selected()
            if switch_off is True:
                wd.find_element(By.CSS_SELECTOR, switch_locator_click).click()

    #  Проверка состояния тумблера
    def assert_switch(self, switch_locator_click, switch_locator_value, mode):
        wd = self.app.wd
        WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, switch_locator_click)))
        switch = wd.find_element(By.CSS_SELECTOR, switch_locator_value).is_selected()
        if mode == 'ON':
            assert switch is True, f"Ожидаемый результат = {True}, Фактический = {switch}"
        elif mode == 'OFF':
            assert switch is False, f"Ожидаемый результат = {False}, Фактический = {switch}"

    #  Проверка текста на странице
    def assert_text_on_page(self, identifier, text_page):
        wd = self.app.wd
        element = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, identifier)))
        element = element.text
        for text in text_page:
            assert text in element, f"Ожидаемый текст: '{text}' отуствует на странице, Фактический текст = {element}"

    #  Клик по тексту через xpath локатор
    def text_click(self, locator):
        wd = self.app.wd
        element = WebDriverWait(wd, 5).until(EC.visibility_of_element_located((By.XPATH, locator)))
        element.click()

    #  Возврат свойст текстового поля
    def state_field(self, field_locator, atribut):
        wd = self.app.wd
        field = WebDriverWait(wd, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "%s" % field_locator)))
        return field.get_attribute(atribut)





