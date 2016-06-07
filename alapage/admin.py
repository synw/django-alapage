# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.contrib.flatpages.models import FlatPage
from django.contrib import messages
from alapage.models import Page
from alapage.forms import PageAdminForm
from alapage.utils import can_see_page
from alapage.conf import USE_JSSOR, USE_REVERSION


if USE_REVERSION:
    from reversion.admin import VersionAdmin
admin_class=admin.ModelAdmin
if USE_REVERSION:
    admin_class=VersionAdmin
@admin.register(Page)
class PageAdmin(admin_class):
    form = PageAdminForm
    date_hierarchy = 'edited'
    search_fields = ['title','url','editor__username']
    list_display = ['url','title','edited','editor','created','published','registration_required', 'staff_only']
    list_select_related = ['editor']
    list_display_links = ['title','url']
    list_filter = ['created','edited','published','registration_required']
    filter_horizontal = ['users_only']
    list_select_related = ['editor']

    
    def get_fieldsets(self, request, obj=None):
        super(PageAdmin, self).get_fieldsets(request, obj)
        jssor_fieldset = ('url','title')
        if USE_JSSOR:
            jssor_fieldset += ('slideshow',)
        fieldsets = (
            (None, {
                'fields': ('content',)
            }),
            (None, {
                'fields': jssor_fieldset
            }),
            (_(u'SEO'), {
                'classes': ('collapse',),
                'fields': ('seo_keywords','seo_description')
            }),
            (_(u'Layout'), {
                'classes': ('collapse',),
                'fields': ('layout', 'template_name')
            }),
            (_(u'Permissions'), {
                'classes': ('collapse',),
                'fields': ('published', 'registration_required', 'groups_only', 'users_only', 'staff_only', 'superuser_only')
            }),
        )
        return fieldsets
    
    
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = ()
        if request.user.has_perm('can_change_page_permissions') is False:
            readonly_fields = ('login_required', 'superuser_only', 'staff_only', 'groups_only', 'users_only')
        return readonly_fields
        
    
    def save_model(self, request, obj, form, change):
        obj.editor = request.user
        obj.save()
        return
          
    def change_view(self, request, object_id):
        page = Page.objects.filter(pk=object_id).prefetch_related('groups_only', 'users_only')[0]
        # check if the view is restricted so that only the allowed users can edit it
        user_can_see_page = can_see_page(page, request.user)
        if user_can_see_page is False:
            return HttpResponseForbidden()
        return super(PageAdmin, self).change_view(request, object_id)
    
    def response_change(self, request, obj):
        if '_inline' in request.POST:
            return HttpResponseRedirect(reverse('page-view', kwargs={"url":obj.url}))
        else:
            return super(PageAdmin, self).response_change(request, obj)

#~ deactivate flatpages admin
admin.site.unregister(FlatPage)

