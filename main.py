from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


def get_webdriver() -> WebDriver:
    options = webdriver.ChromeOptions()
    ret_driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)
    return ret_driver


if __name__ == '__main__':
    driver = get_webdriver()

    driver.get('https://www.google.com')
    print('chrome', driver.title)
    driver.quit()
