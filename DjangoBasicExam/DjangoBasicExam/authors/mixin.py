class PlaceholderAuthorMixin:
    def add_placeholder_and_label(self):
        for field in self.fields:
            if field == 'first_name':
                self.fields[field].widget.attrs.update({'placeholder': 'Enter your first name...'})
                self.fields[field].label = 'First Name:'
            elif field == 'last_name':
                self.fields[field].widget.attrs.update({'placeholder': 'Enter your last name...'})
                self.fields[field].label = 'Last Name:'
            elif field == 'passcode':
                self.fields[field].widget.attrs.update({'placeholder': 'Enter 6 digits...'})
                self.fields[field].label = 'Passcode:'
            elif field == 'pets_number':
                self.fields[field].widget.attrs.update({'placeholder': 'Enter the number of your pets...'})
                self.fields[field].label = 'Pets Number:'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_placeholder_and_label()