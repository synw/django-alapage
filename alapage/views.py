# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.conf import settings
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, View
from django.views.generic.base import RedirectView
from django.utils.html import strip_tags
from django.utils.cache import add_never_cache_headers
from alapage.models import Page


USE_JSSOR=getattr(settings, 'ALAPAGE_USE_JSSOR', False)
USE_PRESENTATIONS=getattr(settings, 'ALAPAGE_USE_ZONGO', False)
USE_THEMES = getattr(settings, 'ALAPAGE_USE_THEMES', False)
BASE_TEMPLATE_PATH = getattr(settings, 'ALAPAGE_BASE_TEMPLATE_PATH', 'base.html')

if USE_JSSOR:
    from jssor.models import Slide
    

def get_template_to_extend(session):
    if USE_THEMES:
        base_template=BASE_TEMPLATE_PATH
        if "theme" in session.keys():
            theme=session['theme']
            template_to_extend="themes/"+theme+"/"+base_template
        else:
            template_to_extend=base_template
        return template_to_extend
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
        #~ get themes
        themes = ()
        current_theme = None
        if USE_THEMES:
            try:
                themes = settings.ALAPAGE_THEMES
            except AttributeError:
                if settings.DEBUG:
                    print '======================================='
                    print 'You must set ALAPAGE_THEMES in settings'
            if "theme" in self.request.session.keys():
                current_theme = self.request.session['theme']
        context['use_themes'] = USE_THEMES
        context['themes'] = themes
        context['current_theme'] = current_theme
        context['flatpage'] = page
        context['slideshow'] = page.slideshow
        context['slides'] = slides
        context['layout'] = layout
        context['presentation'] = presentation
        context['layout_path'] = 'alapage/layouts/'+layout+'/top.html'
        context['template_to_extend'] = get_template_to_extend(self.request.session)
        return context


class HomepageView(PageView):
    pass
"""
class ChangeThemeView(View):
    
    def dispatch(self, request, *args, **kwargs):
        try:
            print "DISPATCH "+self.request.session['theme']
        except:
            print 'DISPATCH'
        return super(ChangeThemeView, self).dispatch(request, *args, **kwargs)
"""

class ChangeThemeView(RedirectView):
    permanent = False
    
    def dispatch(self, request, *args, **kwargs):
        try:
            print "DISPATCH : old theme: "+self.request.session['theme']
        except:
            print 'DISPATCH'
        return super(ChangeThemeView, self).dispatch(request, *args, **kwargs)
    
    def get_redirect_url(self, *args, **kwargs):
        print "REDIRECT"
        theme = self.kwargs['theme']
        if "theme" in self.request.session.keys():
            if not theme == "default":
                self.request.session['theme'] = theme
            else:
                print 'del'
                del self.request.session['theme']
                self.request.session.modified = True
        else:
            if not theme == "default":
                self.request.session['theme'] = theme
        if "theme" in self.request.session.keys():
            print "New theme: "+self.request.session['theme']
        else:
            print "No theme"
        url = strip_tags(self.request.GET['from'])
        if not url.endswith('/') and settings.APPEND_SLASH:
            url += '/'
        return url


    
    