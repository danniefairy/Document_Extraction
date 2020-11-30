import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.ui as ui


class TestDocumentExtractor(unittest.TestCase):
    def setUp(self):
        # driver setting
        options = Options()
        options.add_argument("--disable-notifications")
        self.chrome = webdriver.Chrome('./chromedriver', chrome_options=options)

    def not_busy(self, driver):
        try:
            element = self.chrome.find_element_by_id("result")
        except:
            return False
        return element.get_attribute('value')=="EMPTY\n"

    def test_DocumentExtractorUI(self):
        # access to main page
        self.chrome.get("http://localhost:5000/")

        # get the submit button
        try:
            submit_button = self.chrome.find_element_by_id("submit_button")
            submit_button.click()
        except Exception as e:
            self.chrome.quit()
            raise e

        # submit the empty content
        try:
            ui.WebDriverWait(self.chrome, timeout=15).until(self.not_busy)
        except Exception as e:
            self.chrome.quit()
            raise e
        self.chrome.quit()


if __name__ == '__main__':
    unittest.main()
