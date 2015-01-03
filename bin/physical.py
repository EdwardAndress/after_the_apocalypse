
class Physical(object):

    def __init__(self, mass=0, volume=0, width=0, height=0, depth=0):
        if mass:
            self.mass = mass

        if width and height and depth:
            self.width = width
            self.height = height
            self.depth = depth
            self.volume = width * height * depth
        elif volume:
            self.volume = volume
            self.width = volume ^ 3
            self.height = self.width
            self.depth = self.width

    def set_dims(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth


