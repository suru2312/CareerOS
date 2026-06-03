from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'phone', 'bio', 'location', 'github_url', 'linkedin_url', 'profile_picture',]
        