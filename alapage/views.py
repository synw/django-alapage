# -*- coding: utf-8 -*-

from django.conf import settings
from django.http import Http404
from django.views.generic import TemplateView
from alapage.models import Page

try:
    use_jssor=settings.ALAPAGE_USE_JSSOR
except:
    use_jssor=True
    
if use_jssor:
    from jssor.models import Slide
 

class PageView(TemplateView):
    
    def get_template_names(self):
        template_name = 'alapage/default.html'
        if self.template_name:
            template_name=self.template_name
        return template_name
    
    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        try:
            url = kwargs['url']
        except:
            url = '/'
        if not url.startswith('/'):
            url = '/' + url
        if not url.endswith('/') and settings.APPEND_SLASH:
            url += '/'
        try:
            if use_jssor:
                page = Page.objects.filter(url=url).select_related('slideshow')[0]
            else:
                page = Page.objects.filter(url=url)[0]
            slides = None
            if use_jssor:
                if page.slideshow:
                    slides = Slide.objects.filter(slideshow=page.slideshow)
        except Http404:
            raise Http404
        context['flatpage'] = page
        context['slides'] = slides
        return context


class HomepageView(PageView):
    pass
    
    