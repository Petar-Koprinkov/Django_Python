from django.urls import reverse_lazy
from django.views.generic import CreateView

from DjangoExamPrep2.plants.forms import CreatePlantForm
from DjangoExamPrep2.plants.models import Plant


class CreatePlantView(CreateView):
    model = Plant
    form_class = CreatePlantForm
    context_object_name = 'plant'
    success_url = reverse_lazy('catalogue')
    template_name = 'plants/create-plant.html'

