from django.views.generic import TemplateView
from django.shortcuts import render
from .models import UserModel
# ---- 
import sys
import alSerializer
import os


def OLDhomePageView(request):
    """
    @HACK method to check that we can dynamically load data into the html
    """
    # query data from data folder
    cwd = os.getcwd()
    fName = 'data.pk'
    fName = os.path.join(cwd, 'djUsers', fName)
    # print(fName)
    app = alSerializer.PickleSerializer()
    data = app.fromFile(fName)
    # for user in data:
    l = []
    for user in data:
        s = "Reading from file -> {}\n".format(user)
        l.append(s)
    return render(request, 'home.html', {'content': l})
    
def homePageView(request):
    """
    Home page view. This page dynamically load users from the django sqlite db
    """
    context = {'content': UserModel.objects.all()} # pylint: disable=no-member
    return render(request, 'home.html', context)
    
class AboutPageView(TemplateView): 
    template_name = 'about.html'

