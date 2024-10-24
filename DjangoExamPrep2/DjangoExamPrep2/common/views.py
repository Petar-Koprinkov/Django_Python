from django.views.generic import TemplateView, ListView

from DjangoExamPrep2.plants.models import Plant


class HomePageView(TemplateView):
    template_name = 'plants/home-page.html'


class CatalogPageView(ListView):
    model = Plant
    template_name = 'plants/catalogue.html'
    context_object_name = 'plants'
