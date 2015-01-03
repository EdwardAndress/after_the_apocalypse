__author__ = 'jimnarey'

import world_object


class Discrete(world_object.WorldObject):

    def __init__(self):
        super().__init__()
        self.shape = 'cube'
