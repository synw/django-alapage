from django.test import TestCase
from alapage.models import Page
from jssor.models import Slideshow

# models test
class PageTest(TestCase):

    def create_page(self, url='/mypage/', html='<blink>!!</blink>', layout='xs-12', slideshow=None, presentation=None):
        return Page.objects.create(url=url, html=html, layout=layout, slideshow=slideshow, presentation=presentation)
    
    def test_page_creation(self):
        page=self.create_page()
        self.assertTrue(isinstance(page, Page))
        self.assertEqual(page.url, '/mypage/')
        self.assertEqual(page.html, '<blink>!!</blink>')
        self.assertEqual(page.layout, 'xs-12')
        self.assertTrue(page.published)
    
    #~ slideshows
    def create_slideshow(self, slug="slideshow", template_name="full_width_slider.html", title="Slideshow", width=780, height=300):
        return Slideshow.objects.create(slug=slug, template_name=template_name, title=title, width=width, height=height)

    def test_page_with_slideshow_creation(self):
        slideshow=self.create_slideshow()
        page=self.create_page(slideshow=slideshow)
        self.assertTrue(isinstance(page, Page))
        self.assertTrue(isinstance(slideshow, Slideshow))
    
    #~ client tests
    def test_404_page(self):
        response = self.client.get('/404_not_found/')
        self.assertEqual(response.status_code, 404)
        
    def test_page(self):
        self.create_page()
        resp = self.client.get('/mypage/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('flatpage' in resp.context)
        self.assertTrue('layout' in resp.context)
        self.assertTrue('layout_path' in resp.context)
    
    
    
    