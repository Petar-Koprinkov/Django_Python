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


class EditBookForm(BookBaseForm):
    pass


class DeleteBookForm(BookBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True


class SearchForm(forms.Form):
    title = forms.CharField(
        required=False,
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search for book...',
        })
    )
