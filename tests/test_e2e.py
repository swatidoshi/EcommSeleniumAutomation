from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        """
        This is an end-to-end test file which would execute all steps mentioned below
        - Homepage
        - checkout page (product page)
        - confirm page
        :return:
        """
        log = self.getlogger()
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
        log.info("getting all the card titles")
        cards = checkoutpage.productTitle()
        i = -1

        # this will loop on all products and select product whose name is Blackberry
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getProductFooter()[i].click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

        confirm_page = checkoutpage.check_out_items()
        log.info("entering country name as ind")
        self.driver.find_element(By.ID, "country").send_keys("ind")

        self.verifyLinkPresence ("India")

        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        textMatch = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
        log.info("text received from application is"+textMatch)

        assert ("Success! Thank you!" in textMatch)
