# -*- coding: utf-8 -*-

from django.conf.urls import url
from alapage.views import HomepageView, PageView, PagesmapView


urlpatterns = []

urlpatterns.append(
    url(r'^sitemap/$', PagesmapView.as_view(), name="alapage-map"))
#urlpatterns.append(url(r'^alapage/wizard/$', PageWizardView.as_view(), name="alapage-wizard"))
#urlpatterns.append(url(r'^alapage/wizard/post/$', AddPagePostView.as_view(), name="alapage-wizard-post"))
urlpatterns.append(
    url(r'^(?P<url>.*?)$', PageView.as_view(), name="page-view"))
urlpatterns.append(url(r'^', HomepageView.as_view(), name="home-view"))
