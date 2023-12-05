import re

import settings


class BaseValidator(settings.ValidationError):
    base_regex = re.compile(r'^[a-zA-Z0-9_]+$')
    def __init__(self, object, error_code):
        self.object = object
        self.error_code = error_code

    def error_message(self):
        return f'Объект |{self.object}| {self.ERRORS[self.error_code]}'


class UserValidator(BaseValidator):
    def __init__(self, object, error_code = None):
        super().__init__(object, error_code)
        self.username_regex = re.compile(r'^[а-яА-Я0-9_\-]+$')
        self.tag_regex = re.compile(r'^#[a-zA-Z0-9_]+$')
        self.email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        self.object = object
        self.error_code = error_code

    def validate(self):
        if not self.username_regex.match(self.object.username):
            raise Exception(self.error_message())
        if not self.tag_regex.match(self.object.tag):
            raise Exception(self.error_message())
        if not self.email_regex.match(self.object.email):
            raise Exception(self.error_message())
        if not self.base_regex.match(self.object.password):
            raise Exception(self.error_message())
