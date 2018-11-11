from django.views.generic import TemplateView
from django.shortcuts import render

def test(request):
    return render(request, 'test.html', {'content':['TEST A B C ']})

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        context['name'] = 'Gryffindor'
        return context

class AboutPageView(TemplateView):
    template_name = 'about.html'

    

