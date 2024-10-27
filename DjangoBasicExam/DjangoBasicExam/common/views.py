from django.views.generic import TemplateView, ListView

from DjangoBasicExam.posts.models import Post


class IndexView(TemplateView):
    template_name = 'index.html'


class DashboardView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/dashboard.html'

