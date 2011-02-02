from django.test.client import Client
from django.test import TestCase
from testcups.contact.models import Contact
import unittest
from django.conf import settings


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

