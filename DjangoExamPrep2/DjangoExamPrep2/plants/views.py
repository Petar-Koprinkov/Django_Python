from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from DjangoExamPrep2.plants.forms import CreatePlantForm, EditPlantForm, DeletePlantForm
from DjangoExamPrep2.plants.models import Plant


class CreatePlantView(CreateView):
    model = Plant
    form_class = CreatePlantForm
    context_object_name = 'plant'
    success_url = reverse_lazy('catalogue')
    template_name = 'plants/create-plant.html'


class DetailsPlantView(DetailView):
    model = Plant
    context_object_name = 'plant'
    pk_url_kwarg = "plant_id"
    template_name = 'plants/plant-details.html'


class EditPlantView(UpdateView):
    model = Plant
    form_class = EditPlantForm
    success_url = reverse_lazy('catalogue')
    template_name = 'plants/edit-plant.html'
    pk_url_kwarg = "plant_id"


class DeletePlantView(DeleteView):
    model = Plant
    context_object_name = 'plant'
    pk_url_kwarg = "plant_id"
    template_name = 'plants/delete-plant.html'
    form_class = DeletePlantForm
    success_url = reverse_lazy('catalogue')

    def get_initial(self):
        return self.object.__dict__



