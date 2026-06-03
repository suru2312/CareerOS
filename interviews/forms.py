from django import forms
from .models import Interview


class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = [
            'company_name',
            'round_name',
            'interview_date',
            'mode',
            'result',
            'feedback',
            'questions_asked',
        ]
        widgets = {
            'company_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'e.g. TCS'
                }
            ),

            'round_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Technical Round'
                }
            ),

            'interview_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            'mode': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'result': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'feedback': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4
                }
            ),

            'questions_asked': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 6,
                    'placeholder': 'One question per line'
                }
            ),
        }