from django.test import TestCase
from django.http import HttpRequest
from products.views import home_page


class HomePageTest(TestCase):
    def test_home_page_return_correct_html(self):
        response = self.client.get("/")
        html = response.content.decode('utf-8')
        self.assertIn("<title>WUHAN STARSTONE</title>", html)
        self.assertTrue(html.startswith("<html>"))
        self.assertTrue(html.endswith("</html>"))
