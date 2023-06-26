from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

URL = 'http://localhost:4444/wd/hub'


def get_webdriver() -> WebDriver:
    options = webdriver.ChromeOptions()

    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    ret_driver = webdriver.Remote(command_executor=URL, options=options)
    return ret_driver


if __name__ == '__main__':
    driver = get_webdriver()

    driver.get('https://www.google.com')
    print('google:', driver.title)
    driver.quit()
