from django.core.exceptions import ValidationError
from django.test import TestCase
from products.models import Item, Category


class ItemModelsTest(TestCase):
    def test_default_name(self):
        item = Item()
        self.assertEqual(item.name, "")
    
    def test_item_is_related_to_category(self):
        nuCategory = Category.objects.create(name="NEW Category")
        nuItem = Item(name="NEW Product")
        nuItem.category = nuCategory
        nuItem.save()
        self.assertIn(nuItem, nuCategory.item_set.all())
    
    def test_cannot_save_empty_name_item(self):
        nuCategory = Category.objects.create(name="NEW Category")
        nuItem = Item(category=nuCategory, name="")
        with self.assertRaises(ValidationError):
            nuItem.save()
            # nuItem.full_clean()
    
    def test_duplicate_items_are_invalid(self):
        nuCategory = Category.objects.create(name="NEW Category")
        Item.objects.create(category=nuCategory, name="G602")
        with self.assertRaises(ValidationError):
            item = Item(category=nuCategory, name="G602")
            item.full_clean()
    
    def test_duplicate_identifiers_are_invalid(self):
        nuCategory = Category.objects.create(name="NEW Category")
        item1 = Item.objects.create(category=nuCategory, name="G602")
        item2 = Item(category=nuCategory, name="g602")
        self.assertEqual(item1.identifier, item2.identifier)
        with self.assertRaises(ValidationError):
            item2.full_clean()
    
    def test_get_correct_identifier(self):
        nuItem = Item.objects.create(name="Item 1")
        Item.objects.create(name="Item 2")
        self.assertEqual(nuItem.identifier, "item-1")
    
    def test_get_absolute_url(self):
        nuItem = Item.objects.create(name="NEW Product 1")
        self.assertEqual(nuItem.get_absolute_url(), f"/products/categories/{nuItem.identifier}/")
    
    def test_string_representation(self):
        item = Item(name="Product 1")
        self.assertEqual(str(item), "Product 1")


class CategoryModelsTest(TestCase):
    
    def test_get_correct_identifier(self):
        nuCategory = Category.objects.create(name="Category 1")
        Category.objects.create(name="Category 2")
        self.assertEqual(nuCategory.identifier, 'category-1')
    
    def test_get_absolute_url(self):
        nuCategory = Category.objects.create(name="NEW Category")
        self.assertEqual(nuCategory.get_absolute_url(), f"/products/categories/{nuCategory.identifier}/")
    
    def test_duplicate_identifiers_are_invalid(self):
        nuCategory1 = Category.objects.create(name="NEW Category")
        nuCategory2 = Category(name="new Category")
        self.assertEqual(nuCategory1.identifier, nuCategory2.identifier)
        with self.assertRaises(ValidationError):
            nuCategory2.full_clean()
    
    def test_string_representation(self):
        category1 = Category(name="Category 1")
        self.assertEqual(str(category1), "Category 1")
