import pytest
from selenium import webdriver
import json
import os.path
from oxwall_app import Oxwall
from pages.internal_pages import MainPage
from value_object.user import User
from pychromedriver import chromedriver_path


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    driver.implicitly_wait(5)
    base_url = 'http://127.0.0.1/oxwall/'
    driver.get(base_url)
    yield driver
    # driver.quit()


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
    user = User(username="admin", password="pass", real_name="Admin")
    main_page = MainPage(driver)
    sign_in_page = main_page.sign_in_click()
    sign_in_page.fill_form(user.username, user.password)
    dash_page = sign_in_page.submit()
    yield user
    # dash_page.logout()


posts_text = [
    "1-st post",
    "2-nd post",
    "3-rd post"
    ]


@pytest.fixture(params=posts_text, ids=[str(item) for item in posts_text])
def posts_text(request):
    return request.param


PROJECT_DIR = os.path.dirname(__file__)
filename = os.path.join(PROJECT_DIR, "data", "users.json")

with open(filename, encoding="utf8") as f:
    # user_list = json.load(f
    users = [User(**u) for u in json.load(f)]


@pytest.fixture(params=users, ids=[str(u) for u in users])
def user(request):
    return request.param