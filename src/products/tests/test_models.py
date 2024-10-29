from django.db.utils import IntegrityError

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
            nuItem.full_clean()
    
    def test_duplicate_items_are_invalid(self):
        nuCategory = Category.objects.create(name="NEW Category")
        item1 = Item(category=nuCategory, name="G602")
        item1.full_clean()
        item1.save()
        with self.assertRaises(ValidationError):
            item2 = Item(category=nuCategory, name="G602")
            item2.full_clean()
    
    def test_get_absolute_url(self):
        Category.objects.create(name="NEW Category")
        nuItem = Item(name="NEW Product 1")
        nuItem.full_clean()
        nuItem.save()
        self.assertEqual(nuItem.get_absolute_url(), f"/products/1/")
    
    def test_string_representation(self):
        item = Item(name="Product 1")
        self.assertEqual(str(item), "Product 1")
    
    def test_can_modify_item(self):
        Category.objects.create(name="NEW Category")
        nuItem = Item(name="NEW Product 1")
        nuItem.full_clean()
        nuItem.save()
        nuItem.desc = "it's Product 1"
        nuItem.full_clean()  # should not raise
        nuItem.save()  # should not raise


class CategoryModelsTest(TestCase):
    
    def test_get_absolute_url(self):
        nuCategory = Category(name="NEW Category")
        nuCategory.full_clean()
        nuCategory.save()
        self.assertEqual(nuCategory.get_absolute_url(), f"/products/categories/1/")
    
    def test_duplicate_identifiers_are_invalid(self):
        nuCategory1 = Category(name="NEW Category")
        nuCategory1.full_clean()
        nuCategory1.save()
        nuCategory2 = Category(name="NEW Category")
        with self.assertRaises(ValidationError):
            nuCategory2.full_clean()
        with self.assertRaises(IntegrityError):
            nuCategory2.save()
    
    def test_string_representation(self):
        category1 = Category(name="Category 1")
        self.assertEqual(str(category1), "Category 1")
    
    def test_can_modify_category(self):
        category = Category(name="NEW Category 1")
        category.full_clean()
        category.save()
        category.desc = "it's Category 1"
        category.full_clean()  # should not raise
        category.save()  # should not raise
