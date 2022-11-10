Files
conftest.py contains all the required code to catch failed test cases and make screenshot of the page in case any test case will fail.

pages/base.py contains PageObject pattern implementation for Python.

pages/auth_page.py authorization page for working with autotests.

pages/registration_page.py registration page for working with autotests.

pages/elements.py contains helper class to define web elements on web pages.

autotests_rostelecom.py contains Web UI tests for Rostelecom (https://b2c.passport.rt.ru/)

Autotests description
test_start_page_is_correct

Тест-кейс N-01 Корректное отображение "Стандартной страницы авторизации" Тест не проходит(Bugs-01).Причина- форма авторизации по умолчанию не соответствует требованиям

test_location_of_page_blocks

Тест-кейс N-02 - Проверка элементов в левом и правом блоке страницы Тест не проходит(Bugs-02).Причина - расположение элементов на странице не соответствует ожидаемым требованиям

test_phone_tab

Тест-кейс N-03 Проверка названия таб выбора "Номер" Тест не проходит(Bugs-03).Причина - Таб выбора 'Номер' не соответствует ожидаемым требованиям

test_registration_page_and_continue_button

Тест-кейс N-04 Проверка название кнопки "Продолжить" в форме "Регистрация" Тест не проходит(Bugs-04). Причина - Кнопка должна иметь текст 'Продолжить'

test_registration_page_with_empty_name_field

Тест-кейс N-06 Регистрация пользователя с пустым полем "Имя", появления текста с подсказкой об ошибке

test_registration_with_an_incorrect_value_in_the_name_field

Тест-кейс N-07 Регистрация пользователя с некорректным значением в поле "Имя"(< 2 символов), появление текста с подсказкой об ошибке

test_registration_with_an_incorrect_value_in_the_last_name_field

Тест-кейс N-08 Регистрация пользователя с некорректным значением в поле "Фамилия"(>30 символов), появление текста с подсказкой об ошибке

test_registration_of_an_already_registered_user

Тест-кейс N-09 Регистрация пользователя с уже зарегистрированным номером, отображается оповещающая форма

test_notification_form

Тест-кейс N-10 Проверка кнопки "х" - закрыть всплывающее окно оповещения Тест не проходит (Bugs-10). Причина - "Должна быть кнопка закрыть 'х'"

test_incorrect_password_during_registration

Тест-кейс N-11 Некорректный пароль при регистрации пользователя(< 8 символов), появления текста с подсказкой об ошибке

test_authorization_of_a_user_with_an_invalid_password

Тест-кейс N-12 Вход по неправильному паролю в форме "Авторизация" уже зарегистрированного пользователя, надпись "Забыл пароль" перекрашивается в оранжевый цвет

test_instead_of_cyrillic_invalid_characters

Тест-кейс N-13 Регистрация пользователя в форме "Регистрации" в поле ввода "Фамилия" вместо кириллицы, недопустимые символы

test_password_and_password_confirmation_do_not_match

Тест-кейс N-14 Поле ввода "Пароль" и поле ввода "Подтверждение пароля" в форме "Регистрация" не совпадают

test_invalid_email_or_mobile_phone

Тест-кейс N-15 Не валидный email в поле ввода "Email или мобильный телефон"

test_authorisation_valid

Тест-кейс N-16 Тестирование аутентификации зарегистрированного пользователя

How To Run Tests
Install all requirements:

pip install -r requirements.txt
Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

Run tests:

pytest -v --driver Chrome --driver-path ~/chrome autotests_rostelecom.py
Note: ~/chrome in this example is the file of Selenium WebDriver downloaded and unarchived on step #2.