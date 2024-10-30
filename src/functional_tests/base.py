from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import os

from products.models import Item, Category


class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        test_server = os.environ.get("TEST_SERVER")
        if test_server:
            self.live_server_url = "http://" + test_server
        
        # Set up data for the whole TestCase
        self.category = Category.objects.create(name="Granite", desc="A beautiful granite")
        self.item = Item.objects.create(name="G602", category=self.category, desc="A beautiful G602",
                                        img="images/products/G602.jpeg")
    
    def tearDown(self):
        self.browser.quit()
