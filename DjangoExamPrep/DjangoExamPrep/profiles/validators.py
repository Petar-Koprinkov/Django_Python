from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from django.utils.deconstruct import deconstructible


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
            self.__message = 'Ensure this value contains only letters, numbers, and underscore.'
        else:
            self.__message = value

    def __call__(self, value):
        # TODO: Check for special character
        if value.lower() != slugify(value):
            raise ValidationError(self.message)
