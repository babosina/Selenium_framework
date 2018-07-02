from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest


@pytest.mark.usefixtures("set_up_once", "set_up")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, set_up_once):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login("test@email.com", "abcabc")
        result = self.lp.verify_login_success()
        assert result == True

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
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
