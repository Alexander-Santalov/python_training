import allure
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.Elements import ElementsHelper
from fixture.Buttons import ProjectHelperButtons
from fixture.group import GroupHelper
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.options import Options as YANDEX
from selenium.webdriver.chrome.options import Options as CHROME
from selenium.webdriver.firefox.options import Options as FIREFOX


class Application:

    # Настройка браузеров и взаимодействие с классами помошниками
    def __init__(self, browser, base_url):
        if browser == 'Firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'Chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'Yandex':
            options = webdriver.ChromeOptions()
            binary_yandex_driver_file = 'yandexdriver.exe'
            self.wd = webdriver.Chrome(binary_yandex_driver_file, options=options)
        elif browser == 'Chrome_Headless':
            options = CHROME()
            options.headless = True
            self.wd = webdriver.Chrome(options=options)
        elif browser == 'Firefox_Headless':
            options = FIREFOX()
            options.headless = True
            self.wd = webdriver.Firefox(options=options)
        elif browser == 'Yandex_Headless':
            options = YANDEX()
            options.headless = True
            binary_yandex_driver_file = 'yandexdriver.exe'
            self.wd = webdriver.Chrome(binary_yandex_driver_file, options=options)
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(3)
        self.wd.set_window_size(1920, 1080)
        self.session = SessionHelper(self)
        self.Elements = ElementsHelper(self)
        self.group = GroupHelper(self)
        self.Buttons = ProjectHelperButtons(self)
        self.base_url = base_url

    # Проверка на валидный URL
    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    # Открытие домашней страницы
    def open_home_page(self):
        wd = self.wd
        if wd.current_url is not self.base_url:
            wd.get(self.base_url)


    # Выход из браузера
    def destroy(self):
        wd = self.wd
        self.wd.quit()


    # Выполнение скриншота для отчета Allure
    def get_screen(self):
         wd = self.wd
         allure.attach(wd.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)