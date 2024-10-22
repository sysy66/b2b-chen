from django.test import TestCase
from django.http import HttpRequest
from products.views import home_page


class HomePageTest(TestCase):
    
    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "products/home.html")
    
    def test_uses_products_all_template(self):
        response = self.client.get("/products/")
        self.assertTemplateUsed(response, "products/products_all.html")
