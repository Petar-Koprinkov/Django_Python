from django import forms

from DjangoExamPrep2.profiles.models import Profile


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['profile_picture']


class CreateProfileForm(BaseProfileForm):
    pass