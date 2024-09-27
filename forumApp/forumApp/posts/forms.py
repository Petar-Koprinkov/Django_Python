from django import forms

from forumApp.posts.models import Books


class BookBaseForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

        labels = {
            'title': 'Book Title',
            'author': 'Author Name',
        }


class AddBookForm(BookBaseForm):
    pass


class DeleteBookForm(BookBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True
