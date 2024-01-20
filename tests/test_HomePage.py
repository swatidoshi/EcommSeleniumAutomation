import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, test_get_data):
        """
        This test file will execute form submission along with creating logs of the same.
        """

        log = self.getlogger()
        home_page = HomePage(self.driver)
        log.info("first name is "+test_get_data["firstname"])
        home_page.get_name().send_keys(test_get_data["firstname"])
        home_page.get_email().send_keys(test_get_data["lastname"])

        home_page.get_checkbox().click()

        # select class to handle the options in dropdown
        self.selectOptionByText(home_page.get_gender(), test_get_data["gender"])

        home_page.get_submit().click()

        message = home_page.get_message().text

        assert "success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.get_TestData("TestCase2"))
    def test_get_data(self, request):
        return request.param

