### ECommSeleniumAutomation
#### This is a Selenium automation project testing end to end flow of a website. 
It includes functionalities like form submission, product selection, shop etc.

There a 3 separate Page object files for creating objects of each webpage
1. HomePage.py
2. CheckoutPage.py
3. ConfirmPage.py

TestData package contains python file for Home Page data and an excel demo file:
- exceldemo file is to show how to extract data from an excel sheet
- HomePageData file is to get data for form submission on Home Page
- 'tests' package contains 3 main files - conftest.py, test_e2e.py & test_HomePage.py 
  - In test_e2e file, testing of end to end flow of the website is being done. 
    - Starting with form submission on Home page 
    - followed by adding product to the cart on the Checkout page
    - confirming the order on the confirmation page after selecting the delivery location. 
  - In test_HomePage, we are just testing floe of Home page
