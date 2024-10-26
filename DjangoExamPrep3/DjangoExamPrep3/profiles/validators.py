from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class CustomMinLengthValidator:
    def __init__(self, c_len: int, message=None):
        self.message = message
        self.c_len = c_len

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = 'Username must be at least 3 chars long!'
        else:
            self.__message = value

    def __call__(self, value):
        if len(value) < self.c_len:
            raise ValidationError(self.message)


@deconstructible
class IsAlphaNumericValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = 'Username must contain only letters, digits, and underscores!'
        else:
            self.__message = value

    def __call__(self, value: str):
        if not value.isalnum() or not ('_' in value and value.isalnum()):
            raise ValidationError(self.message)


