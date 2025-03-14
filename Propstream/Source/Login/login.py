from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import configparser



config=configparser.RawConfigParser()
config.read("Propstream/Utils/config.properties")

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.web = WebDriverWait(self.driver, 10)

    def login(self):

        username_field = self.web.until(EC.visibility_of_element_located((By.XPATH,'//input[@name="username"]')))
        username_field.send_keys(config.get('ME', 'username'))
        password_field = self.web.until(EC.visibility_of_element_located((By.XPATH,'//input[@name="password"]')))
        password_field.send_keys(config.get('ME', 'password'))
        time.sleep(1)
        login_button = self.web.until(EC.element_to_be_clickable((By.XPATH, config.get('ME', 'Login_bt'))))
        login_button.click()




