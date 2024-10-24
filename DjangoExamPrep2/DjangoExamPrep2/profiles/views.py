from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from DjangoExamPrep2.profiles.forms import CreateProfileForm
from DjangoExamPrep2.profiles.models import Profile
from DjangoExamPrep2.utils import get_stars, get_profile


class CreateProfileView(CreateView):
    model = Profile
    template_name = 'profile/create-profile.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('catalogue')


class DetailsProfileView(DetailView):
    model = Profile
    template_name = 'profile/profile-details.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stars'] = get_stars()
        return context
