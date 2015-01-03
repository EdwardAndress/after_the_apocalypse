__author__ = 'jimnarey'

import effects
import converters
import physical


class WorldObject(object):

    # For objects created which are not passed to the constructor, e.g. effects, __init__ could include
    # a check to ensure that the correct class exists. Would be better to do this in one go when the game
    # loads - means traversing classes - how?

    def __init__(self):
        self.icon = ''  # For the Gui/inventory.
        self.model = ''  # As above, for gameplay. Is this passed to the class?
        self.name = ''
        self.display_as = ''  # E.g. for fish meat vs. a whole fish, so both can display as fish

        self.attack_effect = effects.DefaultEffect(self)  # Could be single item or list
        self.use_effect = effects.DefaultEffect(self)  # Could be single item or list
        self.consume_effect = effects.DefaultEffect(self)  # Could be single item or list
        self.converters = None  # Could be single item or list
        self.physical = None  # Single object

    def report(self, message):
        print(message)

    def attack(self, target):
        self.attack_effect.execute()

    def use(self, target=None):
        self.use_effect.execute()

    def consume(self, consumer):
        self.consume_effect.execute()

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return self.volume


class Item(WorldObject):

    def __init__(self):
        super().__init__()









