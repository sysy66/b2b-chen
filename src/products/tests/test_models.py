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
    

class Category1ModelTest(TestCase):
    def setUp(self):
        # 创建测试分类
        self.category = Category.objects.create(name='Test Category', desc='Test Description')
    
    def test_category_creation(self):
        # 测试分类创建是否成功
        self.assertEqual(self.category.name, 'Test Category')
        self.assertEqual(self.category.desc, 'Test Description')
    
    def test_string_representation(self):
        # 测试字符串输出
        self.assertEqual(str(self.category), 'Test Category')


class ItemModel1Test(TestCase):
    def setUp(self):
        # 创建测试分类
        self.category = Category.objects.create(name='Test Category')
        # 创建测试项目
        self.item = Item.objects.create(
            name='Test Item',
            size='10mm',
            thickness='20mm',
            colour='30mm',
            desc='Test Item Description',
            category=self.category
        )
    
    def test_item_creation(self):
        # 测试项目创建是否成功
        self.assertEqual(self.item.name, 'Test Item')
        self.assertEqual(self.item.size, '10mm')
        self.assertEqual(self.item.thickness, '20mm')
        self.assertEqual(self.item.colour, '30mm')
        self.assertEqual(self.item.desc, 'Test Item Description')
        self.assertEqual(self.item.category, self.category)
    
    def test_string_representation(self):
        # 测试字符串输出
        self.assertEqual(str(self.item), 'Test Item')
    
    def test_default_values(self):
        # 测试默认值
        item_default = Item.objects.create(name='Default Item', category=self.category)
        self.assertEqual(item_default.size, 'General')
        self.assertEqual(item_default.thickness, 'General')
        self.assertEqual(item_default.colour, 'General')
    
    def test_item_unique_together_constraint(self):
        # 测试唯一约束
        Item.objects.create(
            name='Unique Item',
            size='10mm',
            thickness='20mm',
            colour='30mm',
            category=self.category
        )
        with self.assertRaises(Exception):  # 捕获异常
            Item.objects.create(
                name='Unique Item',
                size='10mm',
                thickness='20mm',
                colour='30mm',
                category=self.category
            )
    
    def test_popularity_flag(self):
        # 测试流行标记
        self.assertFalse(self.item.is_popular)  # 默认值为False
        self.item.is_popular = True
        self.item.save()
        self.assertTrue(self.item.is_popular)  # 更新后应为True
    
    def test_image_field_default(self):
        # 测试图片字段默认值
        self.assertEqual(self.item.img.name, 'images/products/default.jpg')  # 默认图片路径
    
    def test_category_relationship(self):
        # 测试与分类的关系
        self.assertEqual(self.item.category.name, 'Test Category')
    
    def test_create_item_with_blank_description(self):
        # 测试创建项目时描述为空
        item = Item.objects.create(
            name='Blank Description Item',
            category=self.category
        )
        self.assertIsNone(item.desc)  # 验证描述为None
    
    def test_create_item_without_category(self):
        # 测试项目创建没有类别的情况
        # should not raise
        Item.objects.create(
            name='No Category Item',
            size='10mm',
            thickness='20mm',
            colour='30mm',
        )
            