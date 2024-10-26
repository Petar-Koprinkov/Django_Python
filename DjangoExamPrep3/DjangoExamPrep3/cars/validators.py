from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class YearValidator():
    def __init__(self, start_year, end_year, message=None):
        self.start_year = start_year
        self.end_year = end_year
        self.message = message


    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.message = 'Year must be between 1999 and 2030!'
        else:
            self.__message = value

    def __call__(self, value):
        if not self.start_year <= value <= self.end_year:
            raise ValidationError(self.message)