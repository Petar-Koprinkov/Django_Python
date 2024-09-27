from datetime import datetime
from django.shortcuts import render, redirect
from forumApp.posts.forms import AddBookForm
from forumApp.posts.models import Books


def index(request):

    return render(request, 'forum/base.html', )


def dashboard(request):
    books = Books.objects.all()

    context = {"books": books}
    return render(request, 'forum/dashboard.html', context)


def add_book(request):
    form = AddBookForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'forum/add-book.html', context)


def delete_book(request, pk):
    book = Books.objects.get(pk=pk)
    form = AddBookForm(instance=book)

    if request.method == 'POST':
        book.delete()
        return redirect('index')

    context = {
        'form': form,
        'book': book,
    }

    return render(request, 'forum/delete-book.html', context)















