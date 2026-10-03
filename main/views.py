from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from .forms import InquiryForm, ProjectForm, TestimonyForm, TechStackForm  
from .models import Inquiry, PersonalInfo, Project, TechStack, Testimony

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

def admin_login_view(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None and user.is_superuser:
      login(request, user)
      return redirect('dashboard')
    else:
      messages.error(request, 'Access denied. Admin credentials required.')

  return render(request, 'main/admin_login.html')


@user_passes_test(lambda u: u.is_superuser)
def dashboard_view(request):
  projects = Project.objects.all()
  tech_stacks = TechStack.objects.all()
  return render(
      request,
      'main/dashboard.html',
      {'projects': projects, 'tech_stacks': tech_stacks},
  )


@user_passes_test(lambda u: u.is_superuser)
def tech_stack_list(request):
  tech_stacks = TechStack.objects.all()
  return render(request, 'main/tech_stack_list.html', {'tech_stacks': tech_stacks})


@user_passes_test(lambda u: u.is_superuser)
def add_tech_stack(request):
  if request.method == 'POST':
    form = TechStackForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('dashboard')
  else:
    form = TechStackForm()
  return render(request, 'main/add_tech_stack.html', {'form': form})