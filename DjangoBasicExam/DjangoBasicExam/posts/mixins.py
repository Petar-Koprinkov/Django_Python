class PlaceholderPostMixin:
    def add_placeholder_and_label(self):
        for field in self.fields:
            if field == 'title':
                self.fields[field].widget.attrs.update({'placeholder': 'Put an attractive and unique title...'})
                self.fields[field].label = 'Title:'
            elif field == 'image_url':
                self.fields[field].label = 'Post Image URL:'
            elif field == 'content':
                self.fields[field].widget.attrs.update({'placeholder': 'Share some interesting facts about your '
                                                                       'adorable pets...'})
                self.fields[field].label = 'Content:'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_placeholder_and_label()


class ReadOnlyPostMixin:
    def readonly(self):
        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.readonly()
