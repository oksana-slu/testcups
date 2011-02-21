from django.test.client import Client
from django.test import TestCase
from testcups.contact.models import Contact, Middleware
from django.conf import settings
from django.contrib.auth.models import User, Permission, Group, \
                                        Message, ContentType
from django.contrib.sessions.models import Session
from django.contrib.sites.models import Site
from django.contrib.admin.models import LogEntry
from django.core import management
import sys
import re
import os


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


class EditContactTestCase(TestCase):

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
        '''fofm reversed'''
        self.assertTrue(page_edit.content.find('id_skype') <
                        page_edit.content.find('id_last_name'))
        page_edit = self.client.post('/edit_contact/', {'name': 'john'},
                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
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
        self.assertEqual(page_edit.status_code, 302)
        '''check work template tag'''
        self.failUnlessEqual(self.client.login(username='admin',
                                               password='admin'), True)
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 200)
        self.failIfEqual(response.content.find('/admin/contact/contact/1/'),
                                                                       -1)
        '''check work command django-admin'''
        stderr = sys.stderr
        stdout = sys.stdout
        sys.stderr = open('error.log', 'w')
        sys.stdout = open('out.log', 'w')
        management.call_command('printmod')
        sys.stderr = stderr
        sys.stdout = stdout
        a = '''Error: Permission (\d+)
Error: Group (\d+)
Error: User (\d+)
Error: Message (\d+)
Error: ContentType (\d+)
Error: Session (\d+)
Error: Site (\d+)
Error: LogEntry (\d+)
Error: Contact (\d+)
Error: Middleware (\d+)
'''
        f = open('error.log', 'r')
        b = f.read()
        f.close()
        result = re.findall(a, b, re.M)[0]
        perm_c, group_c, user_c, msg_c, ct_c, sess_c, site_c, loge_c, \
        cont_c, middl_c = result
        self.assertEqual(int(perm_c), Permission.objects.all().count())
        self.assertEqual(int(group_c), Group.objects.all().count())
        self.assertEqual(int(user_c), User.objects.all().count())
        self.assertEqual(int(msg_c), Message.objects.all().count())
        self.assertEqual(int(ct_c), ContentType.objects.all().count())
        self.assertEqual(int(sess_c), Session.objects.all().count())
        self.assertEqual(int(site_c), Site.objects.all().count())
        self.assertEqual(int(loge_c), LogEntry.objects.all().count())
        self.assertEqual(int(cont_c), Contact.objects.all().count())
        self.assertEqual(int(middl_c), Middleware.objects.all().count())

        os.remove('error.log')
        os.remove('out.log')


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
