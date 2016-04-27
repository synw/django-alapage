from django.conf.urls import patterns, url
from alapage.views import HomepageView, PageView, ChangeThemeView


urlpatterns = patterns('',
    url(r'^themes/(?P<theme>[-_\w]+)/change/$', ChangeThemeView.as_view(), name="change-theme"),
    url(r'^(?P<url>.*?)$', PageView.as_view(), name="page-view"),
    url(r'^', HomepageView.as_view(), name="home-view"),
)

