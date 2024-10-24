from django import forms

from DjangoExamPrep2.plants.mixins import DisabledMixin
from DjangoExamPrep2.plants.models import Plant


class BasePlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class CreatePlantForm(BasePlantForm):
    pass


class EditPlantForm(BasePlantForm):
    pass


class DeletePlantForm(DisabledMixin, BasePlantForm):
    pass
