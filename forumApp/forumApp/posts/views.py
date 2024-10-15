from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView
from forumApp.posts.forms import AddBookForm, DeleteBookForm, EditBookForm, SearchForm, CommentFormSet
from forumApp.posts.models import Books


class IndexView(TemplateView):
    template_name = 'forum/index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['book'] = 'My_book'
    #     return context


# def index(request):
#     return render(request, 'forum/index.html', )


class DashboardView(ListView, FormView):
    template_name = 'forum/dashboard.html'
    model = Books
    context_object_name = 'books'
    form_class = SearchForm
    success_url = reverse_lazy('dashboard')

    def get_queryset(self):
        queryset = self.model.objects.all()

        if 'title' in self.request.GET:
            query = self.request.GET.get('title')
            queryset = queryset.filter(title__icontains=query)

        return queryset


# def dashboard(request):
#     form = SearchForm(request.GET)
#     books = Books.objects.all()
#     if form.is_valid():
#         books = books.filter(title__icontains=form.cleaned_data['title'])
#
#     context = {
#         'form': form,
#         'books': books,
#     }
#
#     return render(request, 'forum/dashboard.html', context)


class AddBookView(CreateView):
    template_name = 'forum/add-book.html'
    form_class = AddBookForm
    success_url = reverse_lazy('index')
    model = Books
    context_object_name = 'book'


# def add_book(request):
#     form = AddBookForm(request.POST or None, request.FILES or None)
#
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('index')
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'forum/add-book.html', context)

class EditBookView(UpdateView):
    template_name = 'forum/edit-page.html'
    form_class = EditBookForm
    success_url = reverse_lazy('dashboard')
    model = Books
    context_object_name = 'book'

    def get_form_class(self):
        if self.request.user.is_superuser:
            return modelform_factory(Books, fields=('title', 'content', 'author', 'language'))
        else:
            return modelform_factory(Books, fields=('content',))


# def edit_book(request, pk):
#     book = Books.objects.get(pk=pk)
#     form = AddBookForm(instance=book)
#
#     if request.method == 'POST':
#         form = EditBookForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('details-book', pk=book.pk)
#
#     context = {
#         'form': form,
#         'book': book,
#     }
#
#     return render(request, 'forum/edit-page.html', context)


class DeleteBookView(DeleteView):
    context_object_name = 'book'
    model = Books
    success_url = reverse_lazy('index')
    template_name = 'forum/delete-page.html'
    form_class = DeleteBookForm

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        book = Books.objects.get(pk=pk)
        return book.__dict__

# def delete_book(request, pk):
#     book = Books.objects.get(pk=pk)
#     form = DeleteBookForm(instance=book)
#
#     if request.method == 'POST':
#         book.delete()
#         return redirect('index')
#
#     context = {
#         'form': form,
#         'book': book,
#     }
#
#     return render(request, 'forum/delete-page.html', context)


def details_page(request, pk):
    book = Books.objects.get(pk=pk)
    formset = CommentFormSet(request.POST or None)

    if request.method == 'POST':
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.book = book
                    comment.save()
            return redirect('index', pk=book.pk)

    context = {
        'book': book,
        'formset': formset,
    }

    return render(request, 'forum/details-page.html', context)
