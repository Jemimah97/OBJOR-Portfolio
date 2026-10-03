from django import forms
from .models import Project, TechStack, Inquiry, Testimony

class TechStackForm(forms.ModelForm):
    class Meta:
        model = TechStack
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter tech stack name'})
        }

class ProjectForm(forms.ModelForm):
    # Radio buttons para sa tech stacks ayon sa quiz requirement
    tech_stacks = forms.ModelMultipleChoiceField(
        queryset=TechStack.objects.all(),
        widget=forms.RadioSelect, 
        required=True
    )

    class Meta:
        model = Project
        fields = ['project_name', 'description', 'tech_stacks', 'link']
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
        }

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