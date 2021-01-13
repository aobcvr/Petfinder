from enum import Enum


class AnimalChoicesEnum(Enum):
    LARGE = 'Large'
    MEDIUM = 'Medium'
    SMALL = 'Small'

    @classmethod
    def choices(cls):
        return ((x.name, x.value) for x in cls)
