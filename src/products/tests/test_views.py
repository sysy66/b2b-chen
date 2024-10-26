from PIL import Image
from django.test import TestCase

from products.models import Item, Category


class HomePageTest(TestCase):
    
    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "products/home.html")


class ProductsViewTest(TestCase):
    def test_uses_all_p_template(self):
        response = self.client.get("/products/")
        self.assertTemplateUsed(response, "products/all_p.html")
    
    def test_uses_detail_template(self):
        nuItem = Item(name="G602")
        nuItem.full_clean()
        nuItem.save()
        response = self.client.get(f"/products/{nuItem.identifier}/")
        self.assertTemplateUsed(response, "products/detail.html")
    
    def test_displays_item_inf(self):
        nuCategory = Category(name="Quartz")
        nuCategory.full_clean()
        nuCategory.save()
        nuItem = Item(name="G602", desc="G602 is good.", is_popular=True, category=nuCategory)
        nuItem.full_clean()
        nuItem.save()
        response = self.client.get(f"/products/{nuItem.identifier}/")
        self.assertContains(response, "G602")
        self.assertContains(response, "G602 is good.")
        self.assertContains(response, "Quartz")
    
    def test_passes_correct_item_to_template(self):
        other_item = Item(name="G603")
        other_item.full_clean()
        other_item.save()
        correct_item = Item(name="G602")
        correct_item.full_clean()
        correct_item.save()
        response = self.client.get(f"/products/{correct_item.id}/")
        self.assertEqual(response.context["item"], correct_item)


class CategoriesViewTest(TestCase):
    def test_uses_categories_template(self):
        nuCategory = Category(name="Quartz")
        nuCategory.full_clean()
        nuCategory.save()
        response = self.client.get(f"/products/categories/{nuCategory.identifier}/")
        self.assertTemplateUsed(response, "products/categories.html")
    
    def test_displays_category_inf(self):
        nuCategory = Category(name="Quartz", desc="Quartz is welcome.")
        nuCategory.full_clean()
        nuCategory.save()
        response = self.client.get(f"/products/categories/{nuCategory.identifier}/")
        self.assertContains(response, "Quartz")
        self.assertContains(response, "Quartz is welcome.")
    
    def test_displays_only_items_for_that_category(self):
        other_category = Item(name="other Quartz")
        other_category.full_clean()
        other_category.save()
        other_item1 = Item(name="P602", category=other_category)
        other_item1.full_clean()
        other_item1.save()
        other_item2 = Item(name="P603", category=other_category)
        other_item2.full_clean()
        other_item2.save()
        
        correct_category = Item(name="Quartz")
        correct_category.full_clean()
        correct_category.save()
        correct_item1 = Item(name="G602", category=correct_category)
        correct_item1.full_clean()
        correct_item1.save()
        correct_item2 = Item(name="G603", category=correct_category)
        correct_item2.full_clean()
        correct_item2.save()
        
        response = self.client.get(f"/products/categories/{correct_category.identifier}/")
        
        self.assertContains(response, "G602")
        self.assertContains(response, "G603")
        self.assertNotContains(response, "P602")
        self.assertNotContains(response, "P603")
    
    def test_passes_correct_category_to_template(self):
        other_category = Item(name="Quartz 01")
        other_category.full_clean()
        other_category.save()
        correct_category = Item(name="Quartz 03")
        correct_category.full_clean()
        correct_category.save()
        response = self.client.get(f"/products/categories/{correct_category.id}/")
        self.assertEqual(response.context["category"], correct_category)
