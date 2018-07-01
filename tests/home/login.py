from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest


class LoginTest(unittest.TestCase):

    base_url = "https://letskodeit.teachable.com/"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(base_url)
    driver.implicitly_wait(2)
    lp = LoginPage(driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):

        self.lp.login("test@email.com", "abcabc")
        result = self.lp.verify_login_success()
        assert result == True
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalid_login(self):

        self.driver.get(self.base_url)
        self.lp.login("lalalla@mail.com", "abcabcabc")
        result = self.lp.verify_login_failed()
        assert result == True


if __name__ == "__main__":
    """
    Can be run directly from the command line using pytest
    """
    # ff = LoginTest()
    # ff.test_valid_login()
    unittest.main()
