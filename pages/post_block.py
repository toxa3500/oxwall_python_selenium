from selenium.webdriver.common.keys import Keys

from pages.locators import PostLocator
from value_object.user import User


class PostBlock:
    def __init__(self, element):
        self.element = element

    @property
    def text(self):
        return self.element.find_element(*PostLocator.POST_TEXT).text

    @property
    def time(self):
        return self.element.find_element(*PostLocator.POST_TIME).text

    @property
    def user(self):
        user_element = self.element.find_element(*PostLocator.POST_USER)
        real_name = user_element.text
        username = user_element.get_attribute("href").split("/")[-1]
        return User(username=username, real_name=real_name)

    # TODO
    def add_like(self):
        self.element.find_element(*PostLocator.POST_LIKES_BUTTON).click()
        pass

    @property
    def likes_count(self):
        return self.element.find_element(*PostLocator.POST_LIKES_COUNT).text

    @property
    def is_liked(self):
        return "newsfeed_active_button" in self.element.find_element(*PostLocator.POST_LIKES_BUTTON).get_attribute("class")

    def click_add_comment(self):
        self.element.find_element(*PostLocator.POST_COMMENT_BUTTON).click()

    def add_comment(self, text):
        self.element.find_element(*PostLocator.POST_COMMENT_FIELD).send_keys(text)
        self.element.find_element(*PostLocator.POST_COMMENT_FIELD).send_keys(Keys.ENTER)

    def comment_text(self):
        return self.element.find_elements(*PostLocator.POST_COMMENT_TEXT)[-1].text
