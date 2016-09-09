# -*- coding: utf-8 -*-

from django.conf import settings
from django.db.models.query import Prefetch
from django.http import Http404
from django.views.generic import TemplateView
from alapage.models import Page
from alapage.utils import can_see_page
from alapage.conf import BASE_TEMPLATE_PATH, USE_JSSOR


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
        # get the page with 1 query
        self.page_q = Page.objects.filter(url=url)
        if len(self.page_q) == 0:
            raise Http404
        self.page = self.page_q[0]
        # check if other queries are really necessary and get the related data
        if USE_JSSOR is True:
            prefetch = Prefetch("slideshow_group__slideshows", queryset=self.page_q)
            self.page_q = Page.objects.prefetch_related(prefetch)
        if self.page.is_reserved_to_users is True \
        or self.page.is_reserved_to_groups is True\
        or self.page.staff_only is True \
        or self.page.superuser_only is True:
            if self.page.is_reserved_to_users is True:
                prefetch = Prefetch('users_only', queryset=self.page_q)
                self.page_q = Page.objects.prefetch_related(prefetch)
            if self.page.is_reserved_to_groups is True:
                prefetch = Prefetch('groups_only', queryset=self.page_q)
                self.page_q = Page.objects.prefetch_related(prefetch)
            # check permissions
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
        if USE_JSSOR is True:
            slideshow_group = page.slideshow_group
            if page.slideshow_group is not None:
                context['slideshows_group'] = slideshow_group
                context['fullscreen'] = slideshow_group.fullscreen
        context['page'] = page
        context['template_to_extend'] = BASE_TEMPLATE_PATH
        return context


class HomepageView(PageView):
    pass
    