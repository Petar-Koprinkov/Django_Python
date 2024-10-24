from django import forms

from DjangoExamPrep2.plants.models import Plant


class BasePlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class CreatePlantForm(BasePlantForm):
    pass

