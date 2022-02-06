import random
import time
import pytest
import allure



@allure.epic("Тесты Вкладка Адресна книга")
@allure.feature("Проверки на сравнение знченийзначений")
@pytest.mark.flaky()


class TestNetworkValidation():

    @allure.story("Подраздел Группа")
    @allure.title("Проверка имени группы")
    @pytest.mark.parametrize("testdata", [random.randint(1, 100), random.randint(1, 100)])
    def test_save_group(self, app, testdata):
        with allure.step("Создание группы"):
            app.group.open_group_page()
            app.group.create_group(testdata)
        with allure.step("Выход и повторный вход"):
            app.session.logout()
            app.session.login('admin', 'secret')
            app.group.open_group_page()
        with allure.step("Проверка имени группы после сохранения"):
            app.group.assert_name(testdata)


