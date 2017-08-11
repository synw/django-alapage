from django.conf.urls import url
from alapage.views import HomepageView, PageView, PagesmapView


urlpatterns = [
    url(r'^sitemap/?$', PagesmapView.as_view(), name="alapage-map"),
    url(r'^(?P<url>.*?)?$', PageView.as_view(), name="page-view"),
    url(r'^', HomepageView.as_view(), name="home-view"),
]
