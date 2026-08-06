from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Project, PersonalInfo, Inquiry, Testimony
from .forms import ProjectForm, InquiryForm, TestimonyForm

def home(request):
    projects = Project.objects.all()
    return render(request, 'main/home.html', {'projects': projects})

def about(request):
    info = PersonalInfo.objects.first()
    return render(request, 'main/about.html', {'info': info})

def contact(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = InquiryForm()
    return render(request, 'main/contact.html', {'form': form})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'main/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'main/project_detail.html', {'project': project})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'main/add_project.html', {'form': form})

def add_testimony(request):
    if request.method == 'POST':
        form = TestimonyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimony_list')
    else:
        form = TestimonyForm()
    return render(request, 'main/add_testimony.html', {'form': form})

class TestimonyListView(ListView):
    model = Testimony
    template_name = 'main/testimony_list.html'
    context_object_name = 'testimonies'
    ordering = ['-id']

def testimony_detail(request, pk):
    testimony = get_object_or_404(Testimony, pk=pk)
    return render(request, 'main/testimony_detail.html', {'testimony': testimony})