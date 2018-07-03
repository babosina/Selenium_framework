"""
Provides functionality to assert the result

self.check_point.mark_final("Test Name', result, 'Message'
"""
import logging
import utilities.custom_logger as cl
from base import selenium_driver as SeleniumDriver


class TestStatus(SeleniumDriver):

    log = cl.custom_logger(logging.INFO)

    def __init__(self, driver):
        """
        Inits CheckPoint class
        """
        super(TestStatus, self).__init__(driver)
        self.result_list = []

    def set_result(self, result, result_message):
        try:
            if result is not None:
                if result:
                    self.result_list.append("PASS")
                    self.log.info("Verification Successful :: ", result_message)
                else:
                    self.result_list.append("FAILED")
                    self.log.info("Verification Failed :: ", result_message)
            else:
                self.result_list.append("FAILED")
                self.log.info("Verification Failed :: ", result_message)
        except:
            self.result_list.append("FAILED")
            self.log.info("Exception Occurred !!!")

    def mark(self, result, result_message):
        """
        Mark the result of the verification point in a test case
        """
        self.set_result(result, result_message)

    def mark_final(self, test_name, result, result_message):
        """
        Mark the final result of the verification point in a test case
        Needs to be called at least once in a test case
        Should be final test status of the test case
        """
        print()
