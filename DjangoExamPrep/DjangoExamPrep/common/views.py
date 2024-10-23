from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView

from DjangoExamPrep.albums.models import Album
from DjangoExamPrep.profiles.forms import AddProfileForm
from DjangoExamPrep.utils import get_profile_object


class HomeView(ListView, FormView):
    def get_template_names(self):
        obj = get_profile_object()
        if obj is not None:
            return ['profile/home-with-profile.html']
        else:
            return ['profile/home-no-profile.html']

    model = Album
    form_class = AddProfileForm
    success_url = reverse_lazy('home')
    context_object_name = 'albums'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())




