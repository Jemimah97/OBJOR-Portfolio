from django import forms
from .models import Project, Inquiry, Testimony

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'description', 'tech_stack', 'link']

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['first_name', 'last_name', 'contact_number', 'email', 'address', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 bg-[#070d19] border border-blue-900/60 rounded-lg text-blue-100 focus:outline-none focus:border-blue-500'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 bg-[#070d19] border border-blue-900/60 rounded-lg text-blue-100 focus:outline-none focus:border-blue-500'}),
            'contact_number': forms.TextInput(attrs={'class': 'w-full px-4 py-2 bg-[#070d19] border border-blue-900/60 rounded-lg text-blue-100 focus:outline-none focus:border-blue-500'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 bg-[#070d19] border border-blue-900/60 rounded-lg text-blue-100 focus:outline-none focus:border-blue-500'}),
            'address': forms.Textarea(attrs={'class': 'w-full px-4 py-2 bg-[#070d19] border border-blue-900/60 rounded-lg text-blue-100 focus:outline-none focus:border-blue-500', 'rows': 3}),
            'message': forms.Textarea(attrs={'class': 'w-full px-4 py-2 bg-[#070d19] border border-blue-900/60 rounded-lg text-blue-100 focus:outline-none focus:border-blue-500', 'rows': 4}),
        }

class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = ['full_name', 'content']