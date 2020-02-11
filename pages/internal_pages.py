from selenium.webdriver.common.keys import Keys

from pages.base_page import Page


class SignInPage(Page):

    def fill_form(self, username, password):
        self.driver.find_element_by_name('identity').clear()
        self.driver.find_element_by_name('identity').send_keys(username)
        self.driver.find_element_by_name('password').clear()
        password_field = self.driver.find_element_by_name('password')
        password_field.send_keys(password)

    def submit(self):
        password_field = self.driver.find_element_by_name('password')
        password_field.send_keys(Keys.ENTER)
        return DashboardPage(self.driver)

    def sign_in_click(self):
        self.driver.find_element_by_name('submit').click()
        return DashboardPage(self.driver)


class InternalPage(Page):

    def sign_in_click(self):
        sign_in_menu = self.driver.find_element_by_class_name('ow_signin_label')
        sign_in_menu.click()
        return SignInPage(self.driver)


class MainPage(InternalPage):

    pass


class DashboardPage(Page):
    def is_this_page(self):
        return self.driver.find_element_by_class_name('active').text == 'Dashboard'
