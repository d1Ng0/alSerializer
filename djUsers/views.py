from django.views.generic import TemplateView
from django.shortcuts import render
from .models import UserModel

def homePageView(request):
    """
    Home page view. This page dynamically load users from the django sqlite db
    """
    context = {'content': UserModel.objects.all()} # pylint: disable=no-member
    return render(request, 'home.html', context)
    
class AboutPageView(TemplateView): 
    template_name = 'about.html'

