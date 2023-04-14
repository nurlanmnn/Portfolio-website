from django.shortcuts import render
from .models import AboutMe, Experience, Project, Services, Settings
# from django.views.generic import ListView

# Create your views here.

def index(request):
    setting = Settings.objects.first()
    aboutme = AboutMe.objects.first()
    services = Services.objects.first()
    experience = Experience.objects.first()
    projects = Project.objects.all()

    context = {
        'settings': setting,
        'aboutme': aboutme,
        'services': services,
        'experience': experience,
        'projects': projects,
    }
    return render(request, 'index.html', context)
