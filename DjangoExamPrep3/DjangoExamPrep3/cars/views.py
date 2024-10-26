from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from DjangoExamPrep3.cars.forms import CreateCarForm, EditCarForm
from DjangoExamPrep3.cars.models import Car
from DjangoExamPrep3.utils import get_profile


class CreateCarView(CreateView):
    model = Car
    form_class = CreateCarForm
    success_url = reverse_lazy('catalogue')
    template_name = 'cars/car-create.html'

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.owner = get_profile()
        form.save()
        return super().form_valid(form)


class CatalogueView(ListView):
    model = Car
    template_name = 'cars/catalogue.html'
    context_object_name = 'cars'


class DetailCarView(DetailView):
    model = Car
    template_name = 'cars/car-details.html'
    context_object_name = 'car'
    pk_url_kwarg = 'id'





