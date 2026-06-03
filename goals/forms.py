from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = [
            'title',
            'description',
            'target_date',
            'status',
            'priority',
            'progress',
        ]

        widgets = {

            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'e.g. Learn Docker'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4
                }
            ),

            'target_date': forms.DateInput(
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

            'priority': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'progress': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 0,
                    'max': 100
                }
            ),
        }