from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    product = (By.CSS_SELECTOR, ".card-title a")
    productFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkout = (By.XPATH, "//button[@class='btn btn-success']")

    def productTitle(self):
        return self.driver.find_elements(*CheckoutPage.product)

    def getProductFooter(self):
        return self.driver.find_elements(*CheckoutPage.productFooter)

    def check_out_items(self):
        self.driver.find_element(*CheckoutPage.checkout).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
