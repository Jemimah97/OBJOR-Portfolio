from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),

    path('projects/add/', views.add_project, name='add_project'),
    path('testimonies/add/', views.add_testimony, name='add_testimony'),
    path('testimonies/', views.TestimonyListView.as_view(), name='testimony_list'),
    path('testimonies/<int:pk>/', views.testimony_detail, name='testimony_detail'),

    path('admin-login/', views.admin_login_view, name='admin_login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('tech-stacks/', views.tech_stack_list, name='tech_stack_list'),
    path('tech-stacks/add/', views.add_tech_stack, name='add_tech_stack'),
]