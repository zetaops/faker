# coding=utf-8



from .. import BaseProvider

localized = True

__author__ = 'fjzach'


class Provider(BaseProvider):
    classroom_codes = ()

    classroom_types = ()

    classroom_formats = ('{{classroom_code}} {{classroom_type}}',)

    @classmethod
    def classroom_code(cls):
        return cls.random_element(cls.classroom_codes)

    @classmethod
    def classroom_type(cls):
        return cls.random_element(cls.classroom_types)

    def classroom(self):
        pattern = self.random_element(self.classroom_formats)
        return self.generator.parse(pattern)
