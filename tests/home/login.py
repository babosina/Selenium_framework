from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest


class LoginTest(unittest.TestCase):

    def test_valid_login(self):
        base_url = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(2)

        lp = LoginPage(driver)

        lp.login("test@email.com", "abcabc")

        user_icon = driver.find_element_by_xpath(".//div[@id='navbar']//span[text()='Test User']")
        if user_icon is not None:
            print("Login Successful")
        else:
            print("Login Failed")

        driver.quit()


if __name__ == "__main__":
    """
    Can be run directly from the command line using pytest
    """
    # ff = LoginTest()
    # ff.test_valid_login()
    unittest.main()
