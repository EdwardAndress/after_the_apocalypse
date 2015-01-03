__author__ = 'jimnarey'

import world_object


class Organism(world_object.WorldObject):

    def __init__(self):
        super().__init__()

    def consume(self, other):
        self.report('This object has no "consume" effect defined')