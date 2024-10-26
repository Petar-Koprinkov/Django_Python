from django import forms

from DjangoExamPrep3.profiles.models import Profile


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']

        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        }


