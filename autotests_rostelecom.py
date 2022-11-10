import pytest

from pages.auth_page import AuthPage
from pages.registration_page import RegPage


# Тест-кейс N-01 (Bugs-01)
# Корректное отображение "Стандартной страницы авторизации"
@pytest.mark.xfail(reason="Форма авторизации по умолчанию не соответствует требованиям")
def test_start_page_is_correct(web_browser):
    page = AuthPage(web_browser)
    phone_tab_class = page.phone_tab.get_attribute("class")
    assert phone_tab_class == "rt-tab rt-tab--active"
    assert page.phone.is_clickable()
    assert page.password.is_clickable()
    assert page.btn_login.is_clickable()
    assert page.registration_link.is_clickable()
    assert page.auth_title.get_text() == "Авторизация"
    assert page.logo_lk.get_text() == "Личный кабинет"


# Тест-кейс N-02 (Bugs-02)
# Проверка элементов в левом и правом блоке страницы
@pytest.mark.xfail(reason="Расположение элементов на странице не соответствует ожидаемым требованиям")
def test_location_of_page_blocks(web_browser):
    page = AuthPage(web_browser)
    assert page.auth_form.find(timeout=1)
    assert page.lk_form.find(timeout=1)


# Тест-кейс N-03(Bugs-03)
# Проверка названия таб выбора "Номер"
@pytest.mark.xfail(reason="Таб выбора 'Номер' не соответствует ожидаемым требованиям")
def test_phone_tab(web_browser):
    page = AuthPage(web_browser)
    assert page.phone_tab.get_text() == "Номер"


# Тест-кейс N-04(Bugs-04)
# Проверка название кнопки "Продолжить" в форме "Регистрация"
@pytest.mark.xfail(reason="Кнопка должна иметь текст 'Продолжить'")
def test_registration_page_and_continue_button(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    assert reg_page.name_field_text.get_text() == "Имя"
    assert reg_page.last_name_field_text.get_text() == "Фамилия"
    assert reg_page.region_field_text.get_text() == "Регион"
    assert reg_page.email_or_mobile_phone_field_text.get_text() == "E-mail или мобильный телефон"
    assert reg_page.password_field_text.get_text() == "Пароль"
    assert reg_page.password_confirmation_field_text.get_text() == "Подтверждение пароля"
    assert reg_page.continue_button.get_text() == "Продолжить"


# Тест-кейс N-06
# Регистрация пользователя с пустым полем "Имя", появления текста с подсказкой об ошибке
def test_registration_page_with_empty_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('')
    reg_page.last_name_field.send_keys("Фамилия")
    reg_page.email_or_mobile_phone_field.send_keys("test123@mail.ru")
    reg_page.password_field.send_keys("Qazwsx124")
    reg_page.password_confirmation_field.send_keys("Qazwsx124")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# Тест-кейс N-07
# Регистрация пользователя с некорректным значением в поле "Имя"(< 2 символов), появление текста с подсказкой об ошибке
def test_registration_with_an_incorrect_value_in_the_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('А')
    reg_page.last_name_field.send_keys("Фамилия")
    reg_page.email_or_mobile_phone_field.send_keys("test123@mail.ru")
    reg_page.password_field.send_keys("Qazwsx124")
    reg_page.password_confirmation_field.send_keys("Qazwsx124")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# Тест-кейс N-08 Регистрация пользователя с некорректным значением в поле "Фамилия"(>30 символов), появление текста с
# подсказкой об ошибке
def test_registration_with_an_incorrect_value_in_the_last_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Татьяна")
    reg_page.last_name_field.send_keys("фывапролджавыываппвуячсмитьйукенгшщфывапролф")
    reg_page.email_or_mobile_phone_field.send_keys("test123@mail.ru")
    reg_page.password_field.send_keys("Qazwsx124")
    reg_page.password_confirmation_field.send_keys("Qazwsx124")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_last_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# Тест-кейс N-09
# Регистрация пользователя с уже зарегистрированным номером, отображается оповещающая форма
def test_registration_of_an_already_registered_user(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Дмитрий")
    reg_page.last_name_field.send_keys("Лункев")
    reg_page.email_or_mobile_phone_field.send_keys("+79210916809")
    reg_page.password_field.send_keys("Test12345678")
    reg_page.password_confirmation_field.send_keys("Test12345678")
    reg_page.continue_button.click()
    assert reg_page.notification_form.is_visible


# Тест-кейс N-10(Bugs-10)
# Проверка кнопки "х" - закрыть всплывающее окно оповещения
@pytest.mark.xfail(reason="Должна быть кнопка закрыть 'х'")
def test_notification_form(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Дмитрий")
    reg_page.last_name_field.send_keys("Лункев")
    reg_page.email_or_mobile_phone_field.send_keys("+79210916809")
    reg_page.password_field.send_keys("Test12345678")
    reg_page.password_confirmation_field.send_keys("Test12345678")
    reg_page.continue_button.click()
    assert reg_page.login_button.get_text() == 'Войти'
    assert reg_page.recover_password_button.get_text() == 'Восстановить пароль'
    assert reg_page.close_button.get_text() == 'x'


# Тест-кейс N-11
# Некорректный пароль при регистрации пользователя(< 8 символов), появления текста с подсказкой об ошибке
def test_incorrect_password_during_registration(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Раиса")
    reg_page.last_name_field.send_keys("Безымянная")
    reg_page.email_or_mobile_phone_field.send_keys("test123@mail.ru")
    reg_page.password_field.send_keys("оп78")
    reg_page.password_confirmation_field.send_keys("оп78")
    reg_page.continue_button.click()
    assert reg_page.error_message_password.get_text() == "Длина пароля должна быть не менее 8 символов"


# Тест-кейс N-12
# Вход по неправильному паролю в форме "Авторизация" уже зарегистрированного пользователя, надпись "Забыл пароль"
# перекрашивается в оранжевый цвет
def test_authorization_of_a_user_with_an_invalid_password(web_browser):
    page = AuthPage(web_browser)
    page.phone.send_keys('+79210916809')
    page.password.send_keys("Test")
    page.btn_login.click()
    assert page.message_invalid_username_or_password.get_text() == "Неверный логин или пароль"
    assert "rt-link--orange" in page.the_element_forgot_the_password.get_attribute('class')


# Тест-кейс N-13
# Регистрация пользователя в форме "Регистрации" в поле ввода "Фамилия" вместо кириллицы, недопустимые символы
def test_instead_of_cyrillic_invalid_characters(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Кузьма")
    reg_page.last_name_field.send_keys("@@@@!!!")
    reg_page.email_or_mobile_phone_field.send_keys("test123@mail.ru")
    reg_page.password_field.send_keys("Qazwsx124")
    reg_page.password_confirmation_field.send_keys("Qazwsx124")
    reg_page.continue_button.click()
    assert reg_page.message_must_be_filled_in_cyrillic.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."



# Тест-кейс N-14
# Поле ввода "Пароль" и поле ввода "Подтверждение пароля" в форме "Регистрация" не совпадают
def test_password_and_password_confirmation_do_not_match(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Татьяна")
    reg_page.last_name_field.send_keys("Фамилия")
    reg_page.email_or_mobile_phone_field.send_keys("test123@mail.ru")
    reg_page.password_field.send_keys("Test123456789")
    reg_page.password_confirmation_field.send_keys("Test12345")
    reg_page.continue_button.click()
    assert reg_page.message_passwords_dont_match.get_text() == "Пароли не совпадают"


# Тест-кейс N-15
# Не валидный email в поле ввода "Email или мобильный телефон"
def test_invalid_email_or_mobile_phone(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Дмитрий")
    reg_page.last_name_field.send_keys("Лунько")
    reg_page.email_or_mobile_phone_field.send_keys("123456789")
    reg_page.password_field.send_keys("Test123456789")
    reg_page.password_confirmation_field.send_keys("Test123456789")
    reg_page.continue_button.click()
    assert reg_page.message_enter_the_phone_in_the_format.get_text() == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"


# Тест-кейс N-16.
# Тестирование аутентификации зарегистрированного пользователя
def test_authorisation_valid(web_browser):
    page = AuthPage(web_browser)
    page.phone.send_keys('+79210916809')
    page.password.send_keys("Test12345678")
    page.btn_login.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url() \
           and '&client_id=account_b2c#/' in page.get_current_url()
