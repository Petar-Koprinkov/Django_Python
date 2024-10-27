from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class AlphaValidator:

    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = 'Your name must contain letters only!'
        else:
            self.__message = value

    def __call__(self, value: str):
        if not value.isalpha():
            raise ValidationError(self.message)


@deconstructible
class ExactlyNumbersValidator:
    def __init__(self, numbers, message=None):
        self.numbers = numbers
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = f'Your passcode must be exactly {self.numbers} digits!'
        else:
            self.__message = value

    def __call__(self, value):
        if not len(value) == self.numbers or not value.isdigit():
            raise ValidationError(self.message)
