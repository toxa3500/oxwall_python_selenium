import pytest
from selenium import webdriver
import json
import os.path

from db.db_connector import OxwallDB
from oxwall_app import Oxwall
from pages.internal_pages import MainPage
from value_object.user import User
from pychromedriver import chromedriver_path


PROJECT_DIR = os.path.dirname(__file__)




@pytest.fixture(scope="session")
def config():
    with open(os.path.join(PROJECT_DIR, "config.json")) as f:
        return json.load(f)


@pytest.fixture()
def driver(config, selenium):
    # driver = selenium
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    driver.implicitly_wait(5)
    base_url = config["web"]["base_url"]
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
def logged_user(driver, config):
    user = User(**config['web']["user"])
    main_page = MainPage(driver)
    sign_in_page = main_page.sign_in_click()
    sign_in_page.fill_form(user.username, user.password)
    dash_page = sign_in_page.submit()
    yield user
    dash_page.sign_out()


@pytest.fixture(scope="session")
def db(config):
    db = OxwallDB(**config['db'])
    yield db
    db.close()


posts_text = [
    "1-st post",
    "2-nd post",
    "3-rd post"
    ]


@pytest.fixture(params=posts_text, ids=[str(item) for item in posts_text])
def posts_text(request):
    return request.param



filename = os.path.join(PROJECT_DIR, "data", "users.json")

with open(filename, encoding="utf8") as f:
    # user_list = json.load(f
    users = [User(**u) for u in json.load(f)]


@pytest.fixture(params=users, ids=[str(u) for u in users])
def user(request, db):
    user = request.param
    if user.username != "admin":
        db.create_user(user)
    yield user
    if user.username != "admin":
        db.delete_user(user.username)


@pytest.fixture(params=users, ids=[str(u) for u in users])
def user_new(request, db):
    user = request.param
    # if user.username != "admin":
    #     db.create_user(user)
    yield user
    if user.username != "admin":
        db.delete_user(user.username)

