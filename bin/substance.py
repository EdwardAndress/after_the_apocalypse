__author__ = 'jimnarey'

import world_object
from elements import ELEMENTS


class Substance(world_object.WorldObject):

    def __init__(self, mass):
        super().__init__()
        self.mass = mass
        self.state = 'solid'


class Element(Substance):

    def __init__(self, name, mass):
        super().__init__(mass)
        self.name = name
        self.atomic_number = ELEMENTS[name].number
        self.symbol = ELEMENTS[name].symbol
        self.boiling_point = ELEMENTS[name].tboil - 273.15
        self.melting_point = ELEMENTS[name].tmelt - 273.15
        self.density = ELEMENTS[name].density
        self.volume = self.mass / self.density

        if self.melting_point > 21:
            self.state = 'solid'
        elif self.boiling_point < 21:
            self.state = 'gas'
        elif self.melting_point < 21 and self.boiling_point > 21:
            self.state = 'liquid'


