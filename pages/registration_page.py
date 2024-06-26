import random
import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import configurations.config


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver
        self.test_url = "https://demoqa.com/automation-practice-form"

        # Authorization locators:
        self.first_name_input = (By.ID, "firstName")
        self.last_name_input = (By.ID, "lastName")
        self.user_email_input = (By.ID, "userEmail")

        self.gender_female_radio_btn = (By.CSS_SELECTOR, ".custom-radio:nth-child(2) > .custom-control-label")
        self.gender_male_radio_btn = (By.CSS_SELECTOR, ".custom-radio:nth-child(1) > .custom-control-label")
        self.gender_other_radio_btn = (By.CSS_SELECTOR, ".custom-radio:nth-child(3) > .custom-control-label")

        self.user_phone_number_input = (By.ID, "userNumber")

        self.user_date_of_birth_input = (By.ID, "dateOfBirthInput")
        self.year_selector = (By.CSS_SELECTOR, ".react-datepicker__year-select")
        self.month_selector = (By.CSS_SELECTOR, ".react-datepicker__month-select")

        self.user_subjects_input = (By.ID, "subjectsInput")

        self.hobbie_sport_checkbox_btn = (By.CSS_SELECTOR, ".custom-checkbox:nth-child(1) > .custom-control-label")
        self.hobbie_reading_checkbox_btn = (By.CSS_SELECTOR, ".custom-checkbox:nth-child(2) > .custom-control-label")
        self.hobbie_music_checkbox_btn = (By.CSS_SELECTOR, ".custom-checkbox:nth-child(3) > .custom-control-label")

        self.upload_picture_btn = (By.ID, "uploadPicture")

        self.user_current_address_input = (By.ID, "currentAddress")
        self.state_selector = (By.ID, "react-select-3-input")
        self.city_selector = (By.ID, "react-select-4-input")

        self.submit_btn = (By.ID, "submit")

        self.filling_out_sign = (By.ID, "example-modal-sizes-title-lg")
        self.table_modal = (By.CSS_SELECTOR, ".modal-content")

    def open_page(self):
        self.driver.get(self.test_url)
        self.driver.execute_script("window.scrollTo(0,800)")

    def is_element_displayed(self, value):
        try:
            element = self.driver.find_element(value)
            return element.is_displayed()
        except Exception as e:
            print(f"Элемент не найден: {e}")
            return False

    def is_element_not_displayed(self, value):
        try:
            element = self.driver.find_element(value)
            return not element.is_displayed()
        except:
            return True

    def enter_first_name(self, name):
        element = self.driver.find_element(*self.first_name_input)
        element.send_keys(name)

    def enter_last_name(self, lastname):
        element = self.driver.find_element(*self.last_name_input)
        element.send_keys(lastname)

    def enter_user_email(self, email):
        element = self.driver.find_element(*self.user_email_input)
        element.send_keys(email)

    def choose_male_gender(self):
        element = self.driver.find_element(*self.gender_male_radio_btn)
        element.click()

    def choose_the_female_gender(self):
        element = self.driver.find_element(*self.gender_female_radio_btn)
        element.click()

    def choose_the_other_gender(self):
        element = self.driver.find_element(*self.gender_other_radio_btn)
        element.click()

    def enter_phone_number(self, number):
        element = self.driver.find_element(*self.user_phone_number_input)
        element.send_keys(number)

    def enter_date_of_birth(self, year, month, day):
        element = self.driver.find_element(*self.user_date_of_birth_input)
        element.click()
        select_year = Select(self.driver.find_element(*self.year_selector))
        select_year.select_by_visible_text(year)
        select_month = Select(self.driver.find_element(*self.month_selector))
        select_month.select_by_visible_text(month)
        select_day = self.driver.find_element(By.CSS_SELECTOR, f".react-datepicker__day--0{day:02d}")
        select_day.click()

    def enter_user_subjects(self, subjects):
        element = self.driver.find_element(*self.user_subjects_input)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        element.send_keys(subjects)
        element.send_keys(Keys.ENTER)

    def choose_sports_hobbie(self):
        element = self.driver.find_element(*self.hobbie_sport_checkbox_btn)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def choose_music_hobbie(self):
        element = self.driver.find_element(*self.hobbie_music_checkbox_btn)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def choose_reading_hobbie(self):
        element = self.driver.find_element(*self.hobbie_reading_checkbox_btn)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def upload_photo(self, file_path):
        element = self.driver.find_element(*self.upload_picture_btn)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.send_keys(file_path)

    def enter_current_address(self, address):
        element = self.driver.find_element(*self.user_current_address_input)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.send_keys(address)

    def select_state(self, state_name):
        element = self.driver.find_element(*self.state_selector)
        element.send_keys(state_name)
        element.send_keys(Keys.ENTER)

    def select_city(self, city):
        element = self.driver.find_element(*self.city_selector)
        element.send_keys(city)
        element.send_keys(Keys.ENTER)

    def submit_form(self):
        element = self.driver.find_element(*self.submit_btn)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def verify_modal_table(self, expected_data):
        rows = self.driver.find_elements(By.CSS_SELECTOR, 'table.table-dark tbody tr')
        table_data = {}
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            label = cells[0].text.strip()
            value = cells[1].text.strip()
            table_data[label] = value

        for key, expected_value in expected_data.items():
            actual_value = table_data.get(key)
            assert actual_value == expected_value, f"Несоответствие для {key}: ожидалось '{expected_value}', получено '{actual_value}'"
