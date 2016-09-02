from django.conf.urls import url
from alapage.views import HomepageView, PageView
from alapage.conf import STAFFPAGES
if STAFFPAGES is True:
    from staffpages.views import StaffpagesMapView


urlpatterns = []

if STAFFPAGES is True:
    urlpatterns.append(url(r'^staff/pages/$', StaffpagesMapView.as_view(), name="staffpages-map"))

urlpatterns.append(url(r'^(?P<url>.*?)$', PageView.as_view(), name="page-view"))
urlpatterns.append(url(r'^', HomepageView.as_view(), name="home-view"))