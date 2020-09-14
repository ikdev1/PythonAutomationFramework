from selenium import webdriver
import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
import allure



@pytest.mark.usefixtures("test_setup")
class TestLogin():
    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        driver.implicitly_wait(5)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):
        try:
            driver = self.driver
            homePage = HomePage(driver)
            homePage.click_welcome()
            homePage.click_logout()
            x = driver.title
            assert x == "abc"

        except AssertionError as error:
            print("Assertion Error Ocurred")
            print(error)
            # currtime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            # screenshotName = "screenshot_"+currtime
            # from allure.constants import AttachmentType
            # # allure.attach(self.driver.get_screenshot_as_png(),
            # # name = "screenshotName", attachment_type = allure.attachment_type.PNG)
            # allure.attach(self.driver.get_screenshot_as_png(), name="screenshotName",
            #               attachment_type=AttachmentType.PNG)
            raise
        except:
            print("Error")
            raise
        else:
            print("No exception")
        finally:
            print("I am inside finally")