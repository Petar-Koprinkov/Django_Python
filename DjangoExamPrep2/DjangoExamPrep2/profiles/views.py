from django.urls import reverse_lazy
from django.views.generic import CreateView
from DjangoExamPrep2.profiles.forms import CreateProfileForm
from DjangoExamPrep2.profiles.models import Profile


class CreateProfileView(CreateView):
    model = Profile
    template_name = 'profile/create-profile.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('catalogue')