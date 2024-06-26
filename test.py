from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()
chrome_options = Options()

driver.get("https://demoqa.com/automation-practice-form")
url = "https://demoqa.com/automation-practice-form"

assert driver.current_url == url

