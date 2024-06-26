import allure

import configurations.config
from pages.registration_page import RegistrationPage
from configurations.config import *


@allure.title("Заполнение всех полей формы валидными данными")
def test_fill_all_input_fields(browser):
    registration_page = RegistrationPage(browser)
    with allure.step("Открыть страницу с формой"):
        registration_page.open_page()
    with allure.step("Ввести имя в поле 'First Name'"):
        registration_page.enter_first_name(FIRST_NAME)
    with allure.step("Ввести фамилию в поле 'Last Name'"):
        registration_page.enter_last_name(LAST_NAME)
    with allure.step("Ввести электронный почтовый адрес в поле 'Email'"):
        registration_page.enter_user_email(USER_EMAIL)
    with allure.step("Выбрать пол, например 'Male'"):
        registration_page.choose_male_gender()
    with allure.step("Ввести номер телефона в поле 'Mobile'"):
        registration_page.enter_phone_number(USER_PHONE_NUMBER)
    with allure.step("Ввести дату рождения в поле 'Date of Birth'"):
        registration_page.enter_date_of_birth("2005", "March", 7)
    with allure.step("Добавить предметы в поле 'Subjects', например 'English'"):
        registration_page.enter_user_subjects(SUBJECTS[0])
    with allure.step("Выбрать хобби в поле 'Hobbies', например 'Sports'"):
        registration_page.choose_sports_hobbie()
    with allure.step("Загрузить фотографию нажатием на кнопку 'Choose file'"):
        registration_page.upload_photo(PHOTO_PATH)
    with allure.step("Ввести адрес в поле 'Current Address'"):
        registration_page.enter_current_address(CURRENT_ADDRESS)
    with allure.step("Выбрать штат, нажатием на кнопку 'Select State'"):
        registration_page.select_state(STATE_1)
    with allure.step("Выбрать город, нажатием на кнопку 'Select City'"):
        registration_page.select_city(CITY_3)
    with allure.step("Нажать на кнопку 'Submit'"):
        registration_page.submit_form()
    expected_data = configurations.config.all_required_table_data
    with allure.step("В появившейся таблице проверить введенные данные на соответствие"):
        registration_page.verify_modal_table(expected_data)


@allure.title("Заполнение только обязательных полей")
def test_fill_required_input_fields(browser):
    registration_page = RegistrationPage(browser)
    with allure.step("Открыть страницу с формой"):
        registration_page.open_page()
    with allure.step("Ввести имя в поле 'First Name'"):
        registration_page.enter_first_name(FIRST_NAME)
    with allure.step("Ввести фамилию в поле 'Last Name'"):
        registration_page.enter_last_name(LAST_NAME)
    with allure.step("Выбрать пол, например 'Male'"):
        registration_page.choose_male_gender()
    with allure.step("Ввести номер телефона в поле 'Mobile'"):
        registration_page.enter_phone_number(USER_PHONE_NUMBER)
    with allure.step("Нажать на кнопку 'Submit'"):
        registration_page.submit_form()
    with allure.step("Проверить успешное заполнение формы и отображение таблицы с данными"):
        registration_page.is_element_displayed(registration_page.filling_out_sign)


@allure.title("Отправка формы с пустыми полями")
def test_blank_form_submit(browser):
    registration_page = RegistrationPage(browser)
    with allure.step("Открыть страницу с формой"):
        registration_page.open_page()
    with allure.step("Нажать на кнопку 'Submit'"):
        registration_page.submit_form()
    with allure.step("Проверить, что таблица с данными не отображается"):
        registration_page.is_element_not_displayed(registration_page.table_modal)


@allure.title("Отправка формы с вводом некорректных данных в обязательные поля")
def test_filling_incorrect_data_in_required_fields(browser):
    registration_page = RegistrationPage(browser)
    with allure.step("Открыть страницу с формой"):
        registration_page.open_page()
    with allure.step("Ввести некорректное имя в поле 'First Name'"):
        registration_page.enter_first_name(incorrect_first_name)
    with allure.step("Ввести некорректную фамилию в поле 'Last Name'"):
        registration_page.enter_last_name(incorrect_last_name)
    with allure.step("Выбрать пол, например 'Male'"):
        registration_page.choose_male_gender()
    with allure.step("Ввести некорректный номер телефона в поле 'Mobile'"):
        registration_page.enter_phone_number(incorrect_phone_num)
    with allure.step("Нажать на кнопку 'Submit'"):
        registration_page.submit_form()
    with allure.step("Проверить, что таблица с данными не отображается"):
        registration_page.is_element_not_displayed(registration_page.table_modal)


@allure.title("Отправка формы с вводом некорректных данных в необязательные поля")
def test_filling_incorrect_data_in_optional_fields(browser):
    registration_page = RegistrationPage(browser)
    with allure.step("Открыть страницу с формой"):
        registration_page.open_page()
    with allure.step("Ввести имя в поле 'First Name'"):
        registration_page.enter_first_name(FIRST_NAME)
    with allure.step("Ввести фамилию в поле 'Last Name'"):
        registration_page.enter_last_name(LAST_NAME)
    with allure.step("Ввести некорректный электронный почтовый адрес в поле 'Email'"):
        registration_page.enter_user_email(incorrect_email)
    with allure.step("Выбрать пол, например 'Male'"):
        registration_page.choose_male_gender()
    with allure.step("Ввести номер телефона в поле 'Mobile'"):
        registration_page.enter_phone_number(USER_PHONE_NUMBER)
    with allure.step("Ввести некорректную дату рождения в поле 'Date of Birth'"):
        registration_page.enter_date_of_birth("2094", "March", 7)
    with allure.step("Добавить несуществующий значение в поле 'Subjects', например 'Rap'"):
        registration_page.enter_user_subjects(incorrect_subject)
    with allure.step("Загрузить файл формата отличного от стандартных форматов изображений нажатием на кнопку 'Choose file'"):
        registration_page.upload_photo(incorrect_file)
    with allure.step("Ввести адрес в поле 'Current Address'"):
        registration_page.enter_current_address(incorrect_address)
    with allure.step("Выбрать штат, нажатием на кнопку 'Select State'"):
        registration_page.select_state(STATE_1)
    with allure.step("Выбрать город, нажатием на кнопку 'Select City'"):
        registration_page.select_city(CITY_3)
    with allure.step("Нажать на кнопку 'Submit'"):
        registration_page.submit_form()
    with allure.step("Проверить, что таблица с данными не отображается"):
        registration_page.is_element_not_displayed(registration_page.table_modal)






