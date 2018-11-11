from django.urls import path

# from .views import HomePageView, AboutPageView
from .views import *
from django.conf.urls import url, include


urlpatterns = [
    # path('about/', AboutPageView.as_view(), name='about'),
    # path('', HomePageView.as_view(), name='home'),
    url(r'^test/', test, name='test')
]

