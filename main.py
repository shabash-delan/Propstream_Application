from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Propstream.Source.Login.login import LoginPage



def main():
    config = ConfigParser()
    config.read("Propstream/Utils/config.properties")


    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()
    url = config.get('ME', 'base_url')
    if url:

    # Login Page

        driver.get(url)
        login_page = LoginPage(driver)
        login_page.login()

        driver.quit()
    else:
        pass


if __name__ == "__main__":
    main()
