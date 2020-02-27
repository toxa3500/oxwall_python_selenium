from conftest import PROJECT_DIR
from pages.internal_pages import DashboardPage
import pytest
import json
from data.random_string import random_string
import os.path
import time

filename = os.path.join(PROJECT_DIR, "data", "posts.json")


with open(filename, encoding="utf8") as f:
    post_text_list = json.load(f)

for _ in range(3):
    post_text_list.append(random_string(maxlen=1000, spaces=True, whitespases=True))


@pytest.mark.parametrize("input_text", post_text_list)
def test_post_create(logged_user, driver, input_text):
    dashboard_page = DashboardPage(driver)
    old_posts = dashboard_page.posts
    dashboard_page.create_post(input_text)
    dashboard_page.wait_new_post(len(old_posts))
    new_post = dashboard_page.posts[0]
    assert new_post.text == input_text
    assert new_post.time == "within 1 minute"
    assert new_post.user == logged_user


def test_set_like_to_post(logged_user, driver):
    dashboard_page = DashboardPage(driver)
    old_post = dashboard_page.posts[0]
    if old_post.is_liked:
        likes_before = int(old_post.likes_count) - 1
    else:
        likes_before = int(old_post.likes_count) + 1
    old_post.add_like()
    time.sleep(1)
    assert int(old_post.likes_count) == likes_before


def test_add_comment_to_post(logged_user, driver, text="new comment"):
    dashboard_page = DashboardPage(driver)
    old_post = dashboard_page.posts[0]
    old_post.click_add_comment()
    old_post.add_comment(text)
    assert old_post.comment_text() == text


def test_add_comment_to_post2(logged_user, driver, text="new comment"):
    pass


