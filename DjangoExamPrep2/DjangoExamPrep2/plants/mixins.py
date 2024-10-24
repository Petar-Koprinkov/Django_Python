class DisabledMixin():
    def disabled_fields(self):
        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disabled_fields()
