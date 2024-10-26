class ReadOnlyMixin():
    def read_only(self):
        for field in self.fields:
            self.fields[field].widget.attrs["readonly"] = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.read_only()
