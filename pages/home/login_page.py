# from selenium import webdriver
from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_input = "user_email"
    _pwd_input = "user_password"
    _login_btn = "commit"

    # def get_login_link(self):
    #     return self.driver.find_element_by_link_text(self._login_link)
    #
    # def get_email_input(self):
    #     return self.driver.find_element_by_id(self._email_input)
    #
    # def get_pwd_input(self):
    #     return self.driver.find_element_by_id(self._pwd_input)
    #
    # def get_login_btn(self):
    #     return self.driver.find_element_by_name(self._login_btn)

    def click_login_link(self):
        # self.get_login_link().click()
        self.element_click(self._login_link, locator_type="linktext")

    def enter_email(self, email):
        # self.get_email_input().send_keys(email)
        self.element_send_keys(email, self._email_input)

    def enter_pwd(self, pwd):
        # self.get_pwd_input().send_keys(pwd)
        self.element_send_keys(pwd, self._pwd_input)

    def click_login_btn(self):
        # self.get_login_btn().click()
        self.element_click(self._login_btn, locator_type="name")

    def login(self, username, pwd):
        self.click_login_link()
        self.enter_email(username)
        self.enter_pwd(pwd)
        self.click_login_btn()
