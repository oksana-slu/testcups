from django.test.client import Client
from django.test import TestCase
from testcups.middleware.models import Middleware
import unittest


class MiddlewareTestCase(TestCase):

    def setUp(self):
        self.middleware = Middleware.objects.create()

    def testCRUD(self):
        self.middleware1 = Middleware.objects.get(id=1)
        self.assertEqual(self.middleware, self.middleware1)
        self.middleware.delete()
        
    def testhttp(self):
        page = self.client.get('/middleware/')
        self.assertEqual(page.status_code, 200)
        
