import time
import pytest
import allure



@allure.epic("Тесты Вкладка Настройка сети")
@allure.feature("Проверки на ввод значений")
@pytest.mark.flaky()


class TestNetworkValidation():

    @allure.story("Подраздел Общие")
    @allure.title("Проверка на ввод валидных значений в поле 'Имя устройства'")
    def test_valid_input_general(self, app):
        with allure.step("Открытие вкладки Группы"):
            app.group.open_group_page()
            time.sleep(3)





