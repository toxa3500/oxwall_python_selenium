from pages.internal_pages import MainPage


def test_login(driver, user):
    main_page = MainPage(driver)
    sign_in_page = main_page.sign_in_click()
    # sign_in_page.username_field.send_keys(user)
    sign_in_page.fill_form(user.username, user.password)
    dashboard_page = sign_in_page.submit()
    assert dashboard_page.is_this_page()
    assert dashboard_page.user_menu.text == user.real_name


def test_sign_up(driver, user_new):
    main_page = MainPage(driver)
    sign_up_page = main_page.sign_up_click()
    sign_up_page.fill_user_data(user_new)
    sign_up_page.fill_email(user_new)
    sign_up_page.fill_pass_and_repeat_pass_fields(user_new)
    sign_up_page.fill_real_name_field(user_new)
    sign_up_page.chose_gender(male=True)
    sign_up_page.chose_birthday()
    dashboard_page = sign_up_page.submit_form()
    assert dashboard_page.logged_user_real_name in user_new.real_name
