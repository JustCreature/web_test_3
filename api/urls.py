from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (AddSiteView, SiteListView,
                    AddStatusView, SiteDetailView)

app_name = 'api_v1'
urlpatterns = [

    path('sites', SiteListView.as_view(), name='sites'),
    path('sites/<slug:pk>/', SiteDetailView.as_view(), name='site_detail'),
    path('sites/add/', AddSiteView.as_view(), name='site_add'),
    path('sites/status', AddStatusView.as_view(), name='site_status_add'),

]