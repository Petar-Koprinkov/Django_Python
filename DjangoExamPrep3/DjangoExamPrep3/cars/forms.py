from django import forms

from DjangoExamPrep3.cars.models import Car


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner']

        widgets = {
            'image_url': forms.Textarea(attrs={'placeholder': 'https://...'}),
        }


class CreateCarForm(BaseCarForm):
    pass


class EditCarForm(BaseCarForm):
    pass