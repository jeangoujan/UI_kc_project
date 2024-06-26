import os

URL = "https://demoqa.com/automation-practice-form"

FIRST_NAME = "Kairat"
LAST_NAME = "Nurtas"
USER_EMAIL = "knurtas@gmail.com"
USER_PHONE_NUMBER = "7479344214"
CURRENT_ADDRESS = "Улица Сезам, д.228, квартира 1337"
SUBJECTS = ["English", "Maths", "Chemistry", "Computer Science"]

# Incorrect data:
incorrect_first_name = "@Jango_123"
incorrect_last_name = "unChained=)"
incorrect_phone_num = "INCORRECT_NUMBER0"
incorrect_email = "pro100_kairagoogle.com"
incorrect_subject = "Rap"
incorrect_file = os.path.abspath("img/__init__.py")
incorrect_address = "                    "

STATE_1 = "NCR"
STATE_2 = "Uttar Pradesh"
STATE_3 = "Haryana"
STATE_4 = "Rajasthan"

CITY_1 = "Delhi"
CITY_2 = "Gurgaon"
CITY_3 = "Noida"

PHOTO_PATH = os.path.abspath("img/example_photo_KAIROSH.jpg")

all_required_table_data = {
        "Student Name": f"{FIRST_NAME} {LAST_NAME}",
        "Student Email": f"{USER_EMAIL}",
        "Gender": "Male",
        "Mobile": f"{USER_PHONE_NUMBER}",
        "Date of Birth": "07 March,2005",
        "Subjects": "English",
        "Hobbies": "Sports",
        "Picture": "example_photo_KAIROSH.jpg",
        "Address": f"{CURRENT_ADDRESS}",
        "State and City": "NCR Noida"
    }