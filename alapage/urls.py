from django.conf.urls import patterns, url
from alapage.views import HomepageView, PageView


urlpatterns = patterns('',
    url(r'^(?P<url>.*?)$', PageView.as_view(), name="page-view"),
    url(r'^', HomepageView.as_view(), name="home-view"),
)

