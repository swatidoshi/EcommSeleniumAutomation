from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    check_box = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    message = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage

    def get_name(self):
        return self.driver.find_element(*HomePage.name)


    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.check_box)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def get_submit(self):
        return self.driver.find_element(*HomePage.submit)

    def get_message(self):
        return self.driver.find_element(*HomePage.message)