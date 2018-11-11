from django.urls import path

# from .views import HomePageView, AboutPageView
from .views import AboutPageView, homePageView
from django.conf.urls import url, include


urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    url('', homePageView, name='home')
]

