import pytest

import time
from datetime import datetime
from selenium import webdriver as selenium_wd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

Base_URL = "https://petfriends.skillfactory.ru"
User = "melisa_89@mail.ru"
Password = "4dec12mon89"

@pytest.fixture(scope="session")
def selenium_driver(request):
    s = Service(r"/Users/Mariia Protsel/PycharmProjects/chromedriver_win32")
    chrome_options = Options()
    driver = selenium_wd.Chrome(service=s, options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get(Base_URL+'/login')
    WebDriverWait(driver,3).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(User)
    driver.find_element(By.ID, "pass").send_keys(Password)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    yield driver

    driver.quit()


