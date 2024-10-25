from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from DjangoExamPrep2.profiles.forms import CreateProfileForm, EditProfileForm
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


class EditProfileView(UpdateView):
    model = Profile
    template_name = 'profile/edit-profile.html'
    form_class = EditProfileForm
    context_object_name = 'profile'
    success_url = reverse_lazy('details_profile')

    def get_object(self, queryset=None):
        return get_profile()


class DeleteProfileView(DeleteView):
    template_name = 'profile/delete-profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_profile()













