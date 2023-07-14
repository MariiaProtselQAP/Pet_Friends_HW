from selenium.webdriver.common.by import By
from conftest import selenium_driver

Base_URL = "https://petfriends.skillfactory.ru"


def test_show_my_pets(selenium_driver):
    driver = selenium_driver

    driver.find_element(By.CSS_SELECTOR, "a.nav-link[href='/my_pets']").click()
    assert driver.current_url == Base_URL + '/my_pets'

    pets_number = driver.find_element(By.XPATH, '//html/body/div[1]/div/div[1]').text.split('\n')[1].split(": ")[1]
    pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
    assert int(pets_number) == len(pets_count)

    # Проверяем количество фотографий
    images = driver.find_elements(By.CSS_SELECTOR, 'img')

    for i in range(len(images)):
        count = 0

        if images[i].get_attribute('src') != '':
            count += 1

    pets_with_image = int(count)
    assert pets_with_image > int(pets_number)/2

def test_check_description(selenium_driver):
    driver = selenium_driver

    driver.find_element(By.CSS_SELECTOR, "a.nav-link[href='/my_pets']").click()
    assert driver.current_url == Base_URL + '/my_pets'

    pets_number = driver.find_element(By.XPATH, '//html/body/div[1]/div/div[1]').text.split('\n')[1].split(": ")[1]
    pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
    assert int(pets_number) == len(pets_count)
    # Вводим одну переменную, которая включает имя, возраст и породу
    description = driver.find_elements(By.TAG_NAME, 'td')

    for i in range (len(description)):
        assert description[i].text != ' '