from selenium import webdriver
from utilities.test_status import TestStatus
from pages.home.login_page import LoginPage
import unittest
import pytest


@pytest.mark.usefixtures("set_up_once", "set_up")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, set_up_once):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    # Need to verify two vefirication points
    # 1 fails, code will not go to the next verification point
    # If assert fails, is stops current test execution and
    # moves to the next method
    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verify_title()
        self.ts.mark(result1, "Title is incorrect")
        # assert result1 == True
        result2 = self.lp.verify_login_success()
        self.ts.mark_final("test_valid_login", result2, "Login not successful")
        # assert result2 == True

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
