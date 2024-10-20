import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_browse_a_product_page_and_submit_message(self):
        # Edith has heard about a cool new online website WUHAN STARSTONE.
        # She goes to check out its homepage
        self.browser.get("http://localhost:8811/products")
        
        # She notices the page title and header mention WUHAN STARSTONE
        self.assertIn("WUHAN STARSTONE", self.browser.title)
        
        self.fail("Finish the test!")
        
        # She noticed a product code named G602
        
        # She clicked on the product image
        
        # When she hits enter, the page updates, and now the products details
        
        # She noticed that there was a window on the page for submitting information
        
        # She submitted her own information
        
        # Satisfied, she goes back to sleep

if __name__ == "__main__":
    unittest.main()
