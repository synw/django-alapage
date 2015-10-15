from django.contrib import admin
from alapage.models import Page


class PageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Page, PageAdmin)

