import time
from selenium.webdriver.common.by import By
from .base import FunctionalTest


class NewVisitorTest(FunctionalTest):
    def test_can_browse_a_product_page_and_submit_message(self):
        # Edith has heard about a cool new online website WUHAN STARSTONE.
        # She goes to check out its homepage
        self.browser.get(self.live_server_url + '/products/')
        
        # She notices the page title and header mention WUHAN STARSTONE
        self.assertIn("WUHAN STARSTONE", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("WUHAN STARSTONE", header_text)
        
        # She noticed a product code named G602
        product_info = self.browser.find_element(By.LINK_TEXT, "G602")
        print(product_info)
        # product_info = self.browser.find_element(By.TAG_NAME, "p")
        # self.assertEqual(product_info.text, "G602")
        
        # She clicked on the product image
        product_info.click()
        time.sleep(1)
        
        # When she hits enter, the page updates, and now the products details
        gallery = self.browser.find_element(By.CLASS_NAME, "gallery")
        img = gallery.find_element(By.TAG_NAME, "img")
        self.assertTrue(img.get_attribute("alt"), "G602")
        
        # She noticed that there was a window on the page for submitting information
        
        # She submitted her own information
        
        # Satisfied, she goes back to sleep
        self.fail("Finish the test!")
