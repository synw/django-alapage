# -*- coding: utf-8 -*-

from django.conf import settings
from django.http import Http404
from django.views.generic import TemplateView
from alapage.models import Page


USE_JSSOR=getattr(settings, 'ALAPAGE_USE_JSSOR', True)
USE_PRESENTATIONS=getattr(settings, 'ALAPAGE_USE_ALLO', True)
    
if USE_JSSOR:
    from jssor.models import Slide
 

class PageView(TemplateView):
    
    def dispatch(self, request, *args, **kwargs):
        try:
            url = kwargs['url']
        except:
            url = '/'
        if not url.startswith('/'):
            url = '/' + url
        if not url.endswith('/') and settings.APPEND_SLASH:
            url += '/'
        try:
            if USE_JSSOR:
                if USE_PRESENTATIONS:
                    self.page = Page.objects.filter(url=url).select_related('slideshow','presentation')[0]
                else:
                    self.page = Page.objects.filter(url=url).select_related('slideshow')[0]
            else:
                if USE_PRESENTATIONS:
                    self.page = Page.objects.filter(url=url).select_related('presentation')[0]
                else:
                    self.page = Page.objects.filter(url=url)[0]
        except Http404:
            raise Http404
        return super(PageView, self).dispatch(request, *args, **kwargs)
    
    def get_template_names(self):
        template_name = 'alapage/default.html'
        if self.page.template_name:
            template_name=self.page.template_name
        return [template_name]
    
    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        page=self.page
        layout=self.page.layout
        slides=None
        if USE_JSSOR:
            if page.slideshow:
                slides = Slide.objects.filter(slideshow=page.slideshow)
        presentation = None
        if USE_PRESENTATIONS:
                presentation = page.presentation
        if not page.published and not self.request.user.is_superuser():
            raise Http404
        context['flatpage'] = page
        context['slideshow'] = page.slideshow
        context['slides'] = slides
        context['layout'] = layout
        context['presentation'] = presentation
        context['layout_path'] = 'alapage/layouts/'+layout+'/top.html'
        return context


class HomepageView(PageView):
    pass
    
    