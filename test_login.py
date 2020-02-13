from pages.internal_pages import MainPage


def test_login(driver):
    user = "demo"
    password = "demo"

    main_page = MainPage(driver)
    sign_in_page = main_page.sign_in_click()
    # sign_in_page.username_field.send_keys(user)
    sign_in_page.fill_form(user, password)
    dashboard_page = sign_in_page.submit()
    assert dashboard_page.is_this_page()