# coding=utf-8

from .. import BaseProvider

localized = True


class Provider(BaseProvider):
    lectures = []

    @classmethod
    def lecture(cls):
        return cls.random_element(cls.lectures)
