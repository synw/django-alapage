# -*- coding: utf-8 -*-

from django.test import TestCase, override_settings
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from alapage.models import Page
from alapage.admin import PageAdmin, PageAdminForm
from django.core.urlresolvers import reverse

# models test
@override_settings(USE_JSSOR=True)
class PageTest(TestCase):
    
    def create_page(self, url='/mypage/', layout='xs-12', published=True, template_name=''):
        page = Page.objects.create(url=url, layout=layout, published=published, template_name=template_name)
        return page
    
    def test_page_creation(self):
        page=self.create_page()
        self.assertTrue(isinstance(page, Page))
        self.assertEqual(page.url, '/mypage/')
        self.assertEqual(page.layout, 'xs-12')
        self.assertTrue(page.published)
      
    #~ client tests
    def test_404_page(self):
        response = self.client.get(reverse('page-view', kwargs={"url":"/mypage/"}))
        self.assertEqual(response.status_code, 404)
        
    def test_page(self):
        page=self.create_page()
        response = self.client.get(reverse('page-view', kwargs={"url":"/mypage/"}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('page' in response.context)
        self.assertTrue('layout' in response.context)
        self.assertTrue('layout_path' in response.context)
        self.assertTrue(page.published)
        self.assertTemplateUsed(response, 'alapage/default.html')
        
    def test_trailing_slash(self):
        self.create_page(url='/mypage/')
        response = self.client.get('/mypage/')
        self.assertEqual(response.status_code, 200)
        
    def page_not_published(self):
        page=self.create_page(url='/mypage/', published=False)
        response = self.client.get('/mypage/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(page.published)
        
    def test_template_name(self):
        page=self.create_page(url='/mypage/', template_name='alapage/layouts/bottom.html')
        response = self.client.get(reverse('page-view', kwargs={"url":"/mypage/"}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(page.template_name, 'alapage/layouts/bottom.html')
    
    #~ admin
    def test_admin_form(self):
        admin = PageAdmin(Page, AdminSite())
        username = 'test_user'
        pwd = 'secret'
        self.user = User.objects.create_superuser(username, 'myemail@test.com', pwd)
        self.client.login(username=username, password=pwd)
        form_data = {'url':'/mypage/', 'content':'Lorem ipsum','title':'Title'}
        form = PageAdminForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save(commit=True)
        page=Page.objects.get(url='/mypage/')
        response = self.client.get('/admin/')
        request = response.wsgi_request
        admin.save_model(request, page, form, True)
        self.assertTrue(page.editor ,self.user)