# -*- coding: utf-8 -*-

import tempfile
from django.test import TestCase, override_settings
from django.contrib.admin.sites import AdminSite
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from alapage.models import Page
from alapage.admin import PageAdmin, PageAdminForm
from jssor.models import Slideshow

# models test
@override_settings(USE_JSSOR=True)
class PageTest(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
    
    def create_page(self, url='/mypage/', layout='xs-12', published=True, template_name='', slideshow_group='', breakpoints_with_no_header=''):
        return Page.objects.create(url=url, layout=layout, published=published, template_name=template_name, slideshow_group=slideshow_group, breakpoints_with_no_header=breakpoints_with_no_header)
    
    def test_page_creation(self):
        page=self.create_page()
        self.assertTrue(isinstance(page, Page))
        self.assertEqual(page.url, '/mypage/')
        self.assertEqual(page.layout, 'xs-12')
        self.assertTrue(page.published)
    
    #~ slideshows
    #def create_slideshow(self, template_name="full_width_slider.html", title="Slideshow", width=780, height=300):
    #    return Slideshow.objects.create(template_name=template_name, title=title, width=width, height=height)
      
    #~ client tests
    def test_404_page(self):
        response = self.client.get('/404_not_found/')
        self.assertEqual(response.status_code, 404)
        
    def test_page(self):
        page=self.create_page()
        response = self.client.get('/mypage/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('page' in response.context)
        self.assertTrue('layout' in response.context)
        self.assertTrue('layout_path' in response.context)
        self.assertTrue(page.published)
        self.assertTemplateUsed(response, 'alapage/default.html')
        
    def test_trailing_slash(self):
        self.create_page(url='/mypage/')
        response = self.client.get('/mypage')
        self.assertEqual(response.status_code, 200)
        
    def page_not_published(self):
        page=self.create_page(url='/mypage/', published=False)
        response = self.client.get('/mypage/')
        self.assertFalse(page.published)
        self.assertEqual(response.status_code, 404)
        
    def test_template_name(self):
        page=self.create_page(url='/mypage/', template_name='alapage/layouts/bottom.html')
        response = self.client.get('/mypage/')
        self.assertEqual(page.template_name, 'alapage/layouts/bottom.html')
        
    def test_homepage(self):
        self.create_page(url='/')
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        
    def test_page_with_slideshow(self):
        page = self.create_page(url='/', slideshow_group='home', breakpoints_with_no_header='320,360')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(page.slideshow_group, 'home')
        self.assertEqual(page.breakpoints_with_no_header, '320,360')
        self.assertEqual(response.context['breakpoints_with_no_header'], [320, 360])

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
        

        
        
    
    