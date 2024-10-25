from PIL import Image
from django.test import TestCase

from products.models import Item


class HomePageTest(TestCase):
    
    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "products/home.html")


class ProductsViewTest(TestCase):
    def test_uses_products_all_template(self):
        response = self.client.get("/products/")
        self.assertTemplateUsed(response, "products/products_all.html")
    
    def test_displays_product_img(self):
        nuItem = Item.objects.create(name="Test Product")
        image = Image.new("RGB", (100, 100), (255, 255, 255))
        nuItem.img = image
        response = self.client.get(f"/media/{nuItem.img}/")
        self.assertEqual(response.status_code, 200,)
