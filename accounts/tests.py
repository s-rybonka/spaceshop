from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

from accounts.models import Account


class AccountModelTestCase(TestCase):
    '''
    TestCase for Account model
    '''

    def setUp(self):
        ''' Create user for tests

        :return: user
        '''
        user = Account.objects.create(email='root@spaceshop.com')
        user.set_password('secret')
        user.save()

    def test_account_create(self):
        self.assertEquals(Account.objects.filter(email='root@spaceshop.com').count(), 1,
                          'Account instance doesn\'t created')

    def test_account_create_superuser(self):
        self.assertEquals(Account.objects.filter(email='root@spaceshop.com').count(), 1, 'Can not create superuser')

    def test_get_full_name(self):
        user = Account(email='root@spaceshop.com', password='secret')
        self.assertEquals(user.get_full_name(), 'root@spaceshop.com', 'Can not get full name')


class AuthViewsTestCase(TestCase):
    '''
    TestCase for auth views
    '''

    def setUp(self):
        user = Account.objects.create(email='root@spaceshop.com')
        user.set_password('secret')
        user.save()

    def test_sign_up_page(self):
        response = self.client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_sign_in_page(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_sign_out_page(self):
        c = Client()
        c.login(email='root@spaceshop.com', password='secret')
        response = self.client.get(reverse('logout'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/logout.html')
