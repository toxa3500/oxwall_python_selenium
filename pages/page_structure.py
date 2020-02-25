from pages.base_page import Page
from pages.locators import SignInPageLocator, SignUpPageLocator
from selenium.webdriver.support.select import Select


class SignInPageElements(Page):
    @property
    def username_field(self):
        return self.find_element(SignInPageLocator.USERNAME_FIELD)

    @property
    def password_field(self):
        return self.find_element(SignInPageLocator.PASSWORD_FIELD)

    @property
    def sign_in_button(self):
        return self.find_element(SignInPageLocator.SIGN_IN_BUTTON)


class SignUpPageElements(Page):

    @property
    def username_field(self):
        elements = self.find_elements(SignUpPageLocator.USERNAME_FIELD)
        for el in elements:
            if el.size['height'] > 2:
                result = el.find_element_by_class_name("ow_username_validator")
                return result

    @property
    def email_field(self):
        return self.find_element(SignUpPageLocator.EMAIL_FIELD)

    @property
    def pass_field(self):
        return self.find_element(SignUpPageLocator.PASS_FIELD)

    @property
    def repeat_pass_field(self):
        return self.find_element(SignUpPageLocator.REPEAT_PASS_FIELD)

    @property
    def real_name_field(self):
        elements = self.find_elements(SignUpPageLocator.REAL_NAME_FIELD)
        for el in elements:
            if el.size['height'] > 22:
                result = el.find_element_by_xpath("td/input[@type = 'text']")
                return result

    @property
    def male_radio(self):
        elements = self.find_elements(SignUpPageLocator.MALE_RADIO)
        for el in elements:
            if el.size['height'] > 22:
                result = el.find_element_by_xpath("td/ul/li/input[@type = 'radio' and @value = '1']")
                return result

    @property
    def female_radio(self):
        elements = self.find_elements(SignUpPageLocator.FEMALE_RADIO)
        for el in elements:
            if el.size['height'] > 22:
                result = el.find_element_by_xpath("td/ul/li/input[@type = 'radio' and @value = '2']")
                return result

    def chose_birthday(self, day=1, month=1, year='1990'):
        elements = self.find_elements(SignUpPageLocator.DATA_PICKER)
        data_picker = ''
        for el in elements:
            if el.size['height'] > 22:
                data_picker = el
        select_data = Select(data_picker.find_element_by_xpath("td//select[option[text() = 'Day']]"))
        select_data.select_by_index(day)
        select_month = Select(data_picker.find_element_by_xpath("td//select[option[text() = 'Month']]"))
        select_month.select_by_index(month)
        select_year = Select(data_picker.find_element_by_xpath("td//select[option[text() = 'Year']]"))
        select_year.select_by_value(year)

    def submit(self):
        self.find_element(SignUpPageLocator.SUBMIT).click()
