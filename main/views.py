from django.shortcuts import render, get_object_or_404
from .models import Project, PersonalInfo

def home(request):
    projects = Project.objects.all()
    return render(request, 'main/home.html', {'projects': projects})

def about(request):
    info = PersonalInfo.objects.first()
    return render(request, 'main/about.html', {'info': info})

def contact(request):
    return render(request, 'main/contact.html')

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'main/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'main/project_detail.html', {'project': project})