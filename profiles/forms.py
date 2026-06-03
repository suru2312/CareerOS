from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:

        model = Profile

        fields = [
            'full_name',
            'phone',
            'bio',
            'location',
            'github_url',
            'linkedin_url',
            'profile_picture',
        ]

        widgets = {

            'full_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your full name'
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Enter phone number'
                }
            ),

            'location': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your location'
                }
            ),

            'github_url': forms.URLInput(
                attrs={
                    'placeholder': 'https://github.com/username'
                }
            ),

            'linkedin_url': forms.URLInput(
                attrs={
                    'placeholder': 'https://linkedin.com/in/username'
                }
            ),

            'bio': forms.Textarea(
                attrs={
                    'placeholder': 'Tell us about yourself...',
                    'rows': 4
                }
            ),
        }