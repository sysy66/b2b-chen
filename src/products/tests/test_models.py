from django.contrib.auth import get_user_model
from django.test import TestCase
from products.models import Item


class ItemModelsTest(TestCase):
    def test_default_text(self):
        item = Item()
        self.assertEqual(item.name, "")