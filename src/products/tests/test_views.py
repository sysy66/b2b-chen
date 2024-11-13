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
    
    def test_display_all_items(self):
        nuCategory = Category.objects.create(name="Test Category")
        item1 = Item(name="G603", category=nuCategory)
        item1.full_clean()
        item1.save()
        item2 = Item(name="G602", category=nuCategory)
        item2.full_clean()
        item2.save()
        response = self.client.get("/products/")
        self.assertContains(response, item1.name)
        self.assertContains(response, item2.name)
    
    def test_uses_detail_template(self):
        nuCategory = Category.objects.create(name="Test Category")
        nuItem = Item(name="G602", category=nuCategory)
        nuItem.full_clean()
        nuItem.save()
        response = self.client.get(f"/products/{nuItem.slug}/")
        self.assertTemplateUsed(response, "products/detail.html")
    
    def test_displays_item_inf(self):
        nuCategory = Category(name="Quartz")
        nuCategory.full_clean()
        nuCategory.save()
        nuItem = Item(name="G602", desc="G602 is good.", is_popular=True, category=nuCategory)
        nuItem.full_clean()
        nuItem.save()
        response = self.client.get(f"/products/{nuItem.slug}/")
        self.assertContains(response, "G602")
        self.assertContains(response, "G602 is good.")
        self.assertContains(response, "Quartz")
        self.assertContains(response, "/media/images/products/default.jpg")
    
    def test_incorrect_urL_resulting_in_404(self):
        nuCategory = Category(name="Quartz")
        nuCategory.full_clean()
        nuCategory.save()
        nuItem = Item(name="G602", desc="G602 is good.", is_popular=True, category=nuCategory)
        nuItem.full_clean()
        nuItem.save()
        idx = nuItem.pk + 1
        response = self.client.get(f"/products/{idx}/")
        self.assertEqual(response.status_code, 404)
    
    def test_passes_correct_item_to_template(self):
        nuCategory = Category.objects.create(name="Test Category")
        other_item = Item(name="G603", category=nuCategory)
        other_item.full_clean()
        other_item.save()
        correct_item = Item(name="G602", category=nuCategory)
        correct_item.full_clean()
        correct_item.save()
        response = self.client.get(f"/products/{correct_item.slug}/")
        self.assertEqual(response.context["item"], correct_item)


class CategoriesViewTest(TestCase):
    def test_uses_categories_template(self):
        nuCategory = Category(name="Quartz")
        nuCategory.full_clean()
        nuCategory.save()
        response = self.client.get(f"/products/categories/{nuCategory.slug}/")
        self.assertTemplateUsed(response, "products/categories.html")
    
    def test_displays_category_inf(self):
        nuCategory = Category(name="Quartz", desc="Quartz is welcome.")
        nuCategory.full_clean()
        nuCategory.save()
        response = self.client.get(f"/products/categories/{nuCategory.slug}/")
        self.assertContains(response, "Quartz")
        self.assertContains(response, "Quartz is welcome.")
    
    def test_incorrect_urL_resulting_in_404(self):
        nuCategory = Category(name="Quartz", desc="Quartz is welcome.")
        nuCategory.full_clean()
        nuCategory.save()
        idx = nuCategory.pk + 1
        response = self.client.get(f"/products/categories/{idx}/")
        self.assertEqual(response.status_code, 404)
    
    def test_displays_only_items_for_that_category(self):
        other_category = Category(name="other Quartz")
        other_category.full_clean()
        other_category.save()
        other_item1 = Item(name="P602", category=other_category)
        other_item1.full_clean()
        other_item1.save()
        other_item2 = Item(name="P603", category=other_category)
        other_item2.full_clean()
        other_item2.save()
        
        correct_category = Category(name="Quartz")
        correct_category.full_clean()
        correct_category.save()
        correct_item1 = Item(name="G602", category=correct_category)
        correct_item1.full_clean()
        correct_item1.save()
        correct_item2 = Item(name="G603", category=correct_category)
        correct_item2.full_clean()
        correct_item2.save()
        
        response = self.client.get(f"/products/categories/{correct_category.slug}/")
        
        self.assertContains(response, "G602")
        self.assertContains(response, "G603")
        self.assertNotContains(response, "P602")
        self.assertNotContains(response, "P603")
    
    def test_passes_correct_category_to_template(self):
        correct_category = Category(name="Quartz 01")
        correct_category.full_clean()
        correct_category.save()
        other_category = Category(name="Quartz 02")
        other_category.full_clean()
        other_category.save()
        response = self.client.get(f"/products/categories/{correct_category.slug}/")
        self.assertEqual(response.context["category"], correct_category)
