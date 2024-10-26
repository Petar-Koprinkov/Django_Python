from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from DjangoExamPrep3.profiles.forms import CreateProfileForm, EditProfileForm
from DjangoExamPrep3.profiles.models import Profile
from DjangoExamPrep3.utils import get_total_price, get_profile


class CreateProfileView(CreateView):
    model = Profile
    template_name = 'profiles/profile-create.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('catalogue')


class DetailsProfileView(DetailView):
    model = Profile
    template_name = 'profiles/profile-details.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_price'] = get_total_price()
        return context


class EditProfileView(UpdateView):
    model = Profile
    template_name = 'profiles/profile-edit.html'
    success_url = reverse_lazy('details-profile')
    form_class = EditProfileForm

    def get_object(self, queryset=None):
        return get_profile()


class DeleteProfileView(DeleteView):
    success_url = reverse_lazy('home')
    template_name = 'profiles/profile-delete.html'

    def get_object(self, queryset=None):
        return get_profile()




