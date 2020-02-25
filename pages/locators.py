from selenium.webdriver.common.by import By

ACTIVE_LOCATOR = (By.CSS_SELECTOR, ".ow_responsive_menu .active")


class SignInPageLocator:
    USERNAME_FIELD = (By.NAME, 'identity')
    PASSWORD_FIELD = (By.NAME, 'password')
    SIGN_IN_BUTTON = (By.NAME, 'submit')


class SignUpPageLocator:
    USERNAME_FIELD = (By.XPATH, "//tr[td/input[@class = 'ow_username_validator']]")
    EMAIL_FIELD = (By.CLASS_NAME, "ow_email_validator")
    PASS_FIELD = (By.XPATH, "//td/input[@name = 'password']")
    REPEAT_PASS_FIELD = (By.XPATH, "//td/input[@name = 'repeatPassword']")
    REAL_NAME_FIELD = (By.XPATH, "//tr[td/label[text() = 'Real name']]")
    MALE_RADIO = (By.XPATH, "//tr[td/ul/li/input[@type = 'radio' and @value = '1']]")
    FEMALE_RADIO = (By.XPATH, "//tr[td/ul/li/input[@type = 'radio' and @value = '2']]")
    DATA_PICKER = (By.XPATH, "//tr[td//option[text() = 'Day']]")
    SUBMIT = (By.NAME, "joinSubmit")


class DashboardPageLocator:
    POST_TEXT_FIELD = (By.NAME, 'status')


class PostLocator:
    POST_TEXT = (By.CLASS_NAME, 'ow_newsfeed_content')
    POST_USER = (By.CSS_SELECTOR, ".ow_newsfeed_string > a")
    POST_TIME = (By.CSS_SELECTOR, "a.create_time.ow_newsfeed_date")
    POST_LIKES_BUTTON = (By.CLASS_NAME, "ow_miniic_like")
    POST_LIKES_COUNT = (By.CLASS_NAME, "newsfeed_counter_likes")
    POST_COMMENT_BUTTON = (By.CLASS_NAME, "ow_miniic_comment")
    POST_COMMENT_FIELD = (By.CLASS_NAME, "comments_fake_autoclick")
    POST_COMMENT_TEXT = (By.CLASS_NAME, "ow_comments_content")

