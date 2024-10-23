from django import forms

from DjangoExamPrep.mixins import PlaceholderMixin
from DjangoExamPrep.profiles.models import Profile


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class AddProfileForm(PlaceholderMixin, BaseProfileForm):
    pass
