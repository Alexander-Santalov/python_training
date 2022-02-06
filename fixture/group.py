from selenium.webdriver.common.by import By
import time


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, 'groups').click()

    def create_group(self, name):
        wd = self.app.wd
        wd.find_element(By.NAME, 'new').click()
        self.app.Elements.field_enter('input[name="group_name"]', name)
        self.app.Buttons.button_click('input[value="Enter information"]')

    def assert_name(self, name):
        wd = self.app.wd
        self.app.Elements.assert_field_name('span.group', name)
        wd.find_element(By.NAME, 'selected[]').click()
        wd.find_element(By.NAME, 'delete').click()





