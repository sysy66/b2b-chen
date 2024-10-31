from django.test import TestCase
from inquiry.models import ClientInfo, MessageInfo
from django.utils import timezone
import datetime


class ClientInfoModelTest(TestCase):
    def setUp(self):
        # 创建测试用的 ClientInfo 实例
        self.client = ClientInfo.objects.create(
            cli_company='Test Company',
            cli_phone='12345678901',
            cli_email='test0@example.com'
        )
    
    def test_str_method(self):
        # 测试 __str__ 方法
        self.assertEqual(str(self.client), 'Test Company')
    
    def test_was_connected_recently_happy_path(self):
        # 测试最近连接的情况
        self.client.updated_at = timezone.now()
        self.assertTrue(self.client.was_connected_recently)
    
    def test_was_connected_recently_edge_case(self):
        # 测试正好 30 天前更新的情况
        self.client.updated_at = timezone.now() - datetime.timedelta(days=30, seconds=-10)
        self.assertTrue(self.client.was_connected_recently)
    
    def test_was_connected_recently_not_recent(self):
        # 测试超过 30 天更新的情况
        self.client.updated_at = timezone.now() - datetime.timedelta(days=31)
        self.assertFalse(self.client.was_connected_recently)
    
    # 测试正常情况
    def test_client_info_creation(self):
        client = ClientInfo.objects.create(
            cli_company="Test Company",
            cli_phone="1234567890",
            cli_email="test@example.com"
        )
        assert client.cli_company == "Test Company"
        assert client.cli_phone == "1234567890"
        assert client.cli_email == "test@example.com"
        assert client.created_at is not None
    
    # 测试电子邮件唯一性
    def test_client_info_email_uniqueness(self):
        ClientInfo.objects.create(
            cli_company="Test Company",
            cli_phone="1234567890",
            cli_email="test@example.com"
        )
        with self.assertRaises(Exception):
            ClientInfo.objects.create(
                cli_company="Another Company",
                cli_phone="0987654321",
                cli_email="test@example.com"  # 重复电子邮件
            )
    
    # 测试最近连接功能
    def test_was_connected_recently(self):
        client = ClientInfo.objects.create(
            cli_company="Test Company",
            cli_phone="1234567890",
            cli_email="test@example.com"
        )
        client.updated_at = timezone.now() - timezone.timedelta(days=15)
        assert client.was_connected_recently is True
        
        client.updated_at = timezone.now() - timezone.timedelta(days=31)
        assert client.was_connected_recently is False


class MessageInfoModelTest(TestCase):
    def setUp(self):
        # 创建一个 ClientInfo 实例作为外键
        self.client = ClientInfo.objects.create(
            cli_company='Test Company',
            cli_phone='12345678901',
            cli_email='test0@example.com'
        )
        # 创建测试用的 MessageInfo 实例
        self.message = MessageInfo.objects.create(
            msg_subject='Test Subject',
            msg_text='Test Message',
            msg_client=self.client
        )
    
    def test_str_method(self):
        # 测试 __str__ 方法
        self.assertEqual(str(self.message), 'Test Subject')
    
    def test_is_deal_default_false(self):
        # 测试默认值 is_deal
        self.assertFalse(self.message.is_deal)
    
    def test_is_deal_true(self):
        # 测试将 is_deal 设置为 True
        self.message.is_deal = True
        self.message.save()
        self.assertTrue(self.message.is_deal)
    
    def test_created_at(self):
        # 测试创建时间是否正确
        self.assertIsInstance(self.message.created_at, datetime.datetime)
    
    def test_message_info_creation(self):
        client = ClientInfo.objects.create(
            cli_company="Test Company",
            cli_phone="1234567890",
            cli_email="test@example.com"
        )
        
        message = MessageInfo.objects.create(
            msg_subject="Test Subject",
            msg_text="This is a test message.",
            msg_client=client
        )
        
        assert message.msg_subject == "Test Subject"
        assert message.msg_text == "This is a test message."
        assert message.msg_client == client
        assert message.created_at is not None
    
    def test_message_info_deal_status(self):
        client = ClientInfo.objects.create(
            cli_company="Test Company",
            cli_phone="1234567890",
            cli_email="test@example.com"
        )
        
        message = MessageInfo.objects.create(
            msg_subject="Test Subject",
            msg_text="This is a test message.",
            msg_client=client,
            is_deal=False
        )
        
        assert message.is_deal is False
        
        message.is_deal = True
        message.save()
        assert message.is_deal is True
    
    # 测试外键约束
    def test_message_info_client_foreign_key_constraint(self):
        client = ClientInfo.objects.create(
            cli_company="Test Company",
            cli_phone="1234567890",
            cli_email="test@example.com"
        )
        
        message = MessageInfo.objects.create(
            msg_subject="Test Subject",
            msg_text="This is a test message.",
            msg_client=client
        )
        
        client.delete()
        # 确保删除客户端将导致消息不可访问
        with self.assertRaises(MessageInfo.DoesNotExist):
            MessageInfo.objects.get(id=message.id)
