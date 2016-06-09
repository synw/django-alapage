# -*- coding: utf-8 -*-

from django.conf import settings
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, View
from django.views.generic.base import RedirectView
from django.utils.html import strip_tags
from alapage.models import Page
from alapage.utils import can_see_page
from alapage.conf import USE_JSSOR, BASE_TEMPLATE_PATH, ENABLE_PRIVATE_PAGES
    

def get_template_to_extend():
    return BASE_TEMPLATE_PATH
 

class PageView(TemplateView):
    
    def dispatch(self, request, *args, **kwargs):
        # get the page
        try:
            url = kwargs['url']
        except:
            url = '/'
        if not url.startswith('/'):
            url = '/' + url
        if not url.endswith('/') and settings.APPEND_SLASH:
            url += '/'
        if ENABLE_PRIVATE_PAGES is True:
            self.page = get_object_or_404(Page.objects.prefetch_related('groups_only', 'users_only'), url=url)
        else:
            self.page = get_object_or_404(Page.objects.select_related(), url=url)
        # check permissions
        if ENABLE_PRIVATE_PAGES is True:
            if can_see_page(self.page, request.user) is False:
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
        if not page.published and not self.request.user.is_superuser:
            raise Http404
        layout=self.page.layout
        if page.breakpoints_with_no_header:
            bnh = []
            for bp in page.breakpoints_with_no_header.split(','):
                bnh.append(int(str.rstrip(str(bp)))) 
            context['breakpoints_with_no_header'] = bnh
            print str(context['breakpoints_with_no_header'])
        context['page'] = page
        context['layout'] = layout
        context['layout_path'] = 'alapage/layouts/'+layout+'/top.html'
        context['template_to_extend'] = get_template_to_extend()
        return context


class HomepageView(PageView):
    pass



    
    