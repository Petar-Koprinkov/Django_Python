from django import forms

from DjangoBasicExam.authors.mixin import PlaceholderAuthorMixin
from DjangoBasicExam.authors.models import Author


class BaseAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'passcode', 'pets_number']


class CreateAuthorForm(PlaceholderAuthorMixin, BaseAuthorForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'passcode', 'pets_number']

        widgets = {
            'passcode': forms.PasswordInput(),
        }


class EditAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'pets_number', 'info', 'image_url']
