from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class CapitalLetterValidator:
    def __init__(self, message=None):
        self.message = message


    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value: str):
        if value is None:
            self.__message = 'Your name must start with a capital letter!'
        else:
            self.__message = value

    def __call__(self, value: str):
        if value != value.capitalize():
            raise ValidationError(self.message)