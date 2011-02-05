from django.test.client import Client
from django.test import TestCase
from testcups.contact.models import Contact, Middleware
import unittest
from django.conf import settings
from django.contrib.auth.models import User


class ContactTestCase(TestCase):

    def setUp(self):
        self.contact = Contact.objects.create(name="alex", last_name="ivanov",
                  birth="2011-01-02", bio="qwertyuiop", email="alex@gmail.com",
                  jabber="jabber", skype="skype", other_contacts="no")

    def testCRUD(self):
        self.contact1 = Contact.objects.get(name="alex")
        self.assertEqual(self.contact, self.contact1)
        self.contact.delete()
        self.contact2 = Contact.objects.filter(name="alex")
        self.assertEqual(self.contact2.count(), 0)

    def testhttp(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        word = page.content.find('jabber')
        self.assertNotEqual(word, -1)
        word1 = page.content.find('noword')
        self.assertEqual(word1, -1)
        word_context = page.content.find(settings.TIME_ZONE)
        self.assertNotEqual(word_context, -1)


'''test for t5_edit_contact'''
'''class EditContactTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com',
                                             'johnpassword')

    def testhttp(self):
        page_login = self.client.post('/accounts/login/',
                            {'username': 'john', 'password': 'johnpassword'})
        self.assertEqual(page_login.status_code, 302)
        message = page_login.content.find('match')
        self.assertEqual(message, -1)
        page_edit = self.client.get('/edit_contact/')
        self.assertEqual(page_edit.status_code, 200)
        word = page_edit.content.find('oksana')
        self.assertNotEqual(word, -1)
        page_edit = self.client.post('/edit_contact/', {'name': 'john'})
        word = page_edit.content.find('john')
        self.assertNotEqual(word, -1)
        page_login = self.client.post('/accounts/login/',
                            {'username': '', 'password': ''})
        self.assertEqual(page_login.status_code, 200)
        message = page_login.content.find('match')
        self.assertNotEqual(message, -1)
        page_logout = self.client.post('/logout/')
        self.assertEqual(page_logout.status_code, 200)
        page_edit = self.client.get('/edit_contact/')
        self.assertEqual(page_edit.status_code, 302)'''


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
