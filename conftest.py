import pytest
from selenium import webdriver

from oxwall_app import Oxwall
from pages.internal_pages import MainPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    base_url = 'https://demo.oxwall.com'
    # base_url = 'http://127.0.0.1/oxwall/'
    driver.get(base_url)
    yield driver
    driver.quit()


@pytest.fixture()
def app(driver):
    return Oxwall(driver)


# @pytest.fixture()
# def logged_user(driver, app):
#     username = "admin"
#     app.login_as(username, "pass")
#     yield username
#     app.logout()


@pytest.fixture()
def logged_user(driver):
    main_page = MainPage(driver)
    username = "demo"
    password = "demo"

    sign_in_page = main_page.sign_in_click()
    dash_page = sign_in_page.fill_form(username, password)
    sign_in_page.sign_in_click()
    yield username
    # dash_page.logout()

posts_text = [
    "1-st post",
    "2-nd post",
    "3-rd post"
    ]


@pytest.fixture(params=posts_text, ids=[str(item) for item in posts_text])
def posts_text(request):
    return request.param

