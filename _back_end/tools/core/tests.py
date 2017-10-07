from django.test import TestCase
from rest_framework.test import APIRequestFactory

from .models import Tools

# Create your tests here.

class TestTools(TestCase):

    def setUp(self):
        Tools.objects.create(title="Test tool 1", url="//localhost/test1", description='test1')
        Tools.objects.create(title="Test tool 2", url="//localhost/test2", description='test2')

    def test_tool_model(self):
        test1 = Tools.objects.get(pk=1)
        test2 = Tools.objects.get(pk=2)

        self.assertEqual(test1.title, "Test tool 1")
        self.assertEqual(test2.title, "Test tool 2")
        self.assertEqual(test1.url, "//localhost/test1")
        self.assertEqual(test2.url, "//localhost/test2")
    
    # def test_serializer(self):
        


        