from django.urls import reverse_lazy
from django.views.generic import CreateView

from DjangoExamPrep3.profiles.forms import CreateProfileForm
from DjangoExamPrep3.profiles.models import Profile


class CreateProfileView(CreateView):
    model = Profile
    template_name = 'profiles/profile-create.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('catalogue')