from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = JobApplication

        fields = [
            'company_name',
            'position',
            'job_url',
            'application_date',
            'status',
            'notes',
        ]

        widgets = {
            'company_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'e.g. TCS'
                }
            ),

            'position': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'e.g. Python Developer'
                }
            ),

            'job_url': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Paste job URL'
                }
            ),

            'application_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            'status': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'notes': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Interview notes, referral details, etc.'
                }
            ),
        }