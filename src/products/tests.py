from django.test import TestCase
from django.http import HttpRequest
from products.views import home_page


class HomePageTest(TestCase):
    
    def test_use_home_page(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "products/home.html")
    
    def test_use_products_all_page(self):
        response = self.client.get("/products/")
        self.assertTemplateUsed(response, "products/products_all.html")
