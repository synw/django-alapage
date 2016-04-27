# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.conf import settings
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, View
from django.views.generic.base import RedirectView
from django.utils.html import strip_tags
from alapage.models import Page
from alapage.conf import USE_JSSOR, USE_PRESENTATIONS, BASE_TEMPLATE_PATH


if USE_JSSOR:
    from jssor.models import Slide
    

def get_template_to_extend():
    return BASE_TEMPLATE_PATH
 

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
        if USE_JSSOR:
            if USE_PRESENTATIONS:
                self.page = get_object_or_404(Page.objects.select_related('slideshow','presentation'), url=url)
            else:
                self.page = get_object_or_404(Page.objects.select_related('slideshow'), url=url)
        else:
            if USE_PRESENTATIONS:
                self.page = get_object_or_404(Page.objects.select_related('presentation'), url=url)
            else:
                self.page = get_object_or_404(Page, url=url)
                #self.page = Page.objects.filter(url=url)[0]
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
        if USE_JSSOR:
            context['slideshow'] = page.slideshow
            context['slides'] = slides
        context['layout'] = layout
        context['presentation'] = presentation
        context['layout_path'] = 'alapage/layouts/'+layout+'/top.html'
        context['template_to_extend'] = get_template_to_extend()
        return context


class HomepageView(PageView):
    pass



    
    