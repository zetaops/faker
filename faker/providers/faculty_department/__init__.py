# coding=utf-8

from .. import BaseProvider

localized = True


class Provider(BaseProvider):
    faculty_departments = []

    @classmethod
    def faculty_department(cls):
        return cls.random_element(cls.faculty_departments)
