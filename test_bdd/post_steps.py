from pytest_bdd import given, when, then

from pages.internal_pages import DashboardPage, MainPage
from value_object.user import User


@given("initial amount of post in Oxwall database")
def initial_posts(driver, app):
    # Должна быть использована фикстура, которая эти посты создает через БД
    # dashboard_page = DashboardPage(driver)
    return app.dashboard_page.posts


@given("I as a logged user")
def logged_user(driver, config, app):
    user = User(**config["web"]["user"])
    # main_page = MainPage(driver)
    app.main_page.sign_in_click()
    app.sign_in_page.fill_form(user.username, user.password)
    app.sign_in_page.submit()
    return user


@when("I add a new post with <text> in Dashboard page")
def create_post(driver, app, text, ):
    # dashboard_page = DashboardPage(driver)
    app.dashboard_page.create_post(text)


@then("a new post block appears before old table of posts")
def wait_new_post(driver, app, initial_posts):
    # dashboard_page = DashboardPage(driver)
    app.dashboard_page.wait_new_post(len(initial_posts))


@then("this post block has this <text> and author as this user and time \"within 1 minute\"")
def verify_new_post(app, text, logged_user):
    new_post = app.dashboard_page.posts[0]
    assert new_post.text == text
    assert new_post.time == "within 1 minute"
    assert new_post.user == logged_user
