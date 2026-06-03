from django import forms
from .models import LearningItem

class LearningItemForm(forms.ModelForm):
    class Meta:
        model = LearningItem
        fields = [
            'title',
            'platform',
            'status',
            'progress',
            'notes',
        ]

        widgets = {

            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'e.g. Django Masterclass'
                }
            ),

            'platform': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'e.g. Udemy'
                }
            ),

            'status': forms.Select(
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

            'notes': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4
                }
            ),
        }