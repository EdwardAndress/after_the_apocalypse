__author__ = 'jimnarey'


class Effect(object):

    def __init__(self, parent):
        self.parent = parent
        pass


class DefaultEffect(Effect):

    def __init__(self, parent):
        super().__init__(parent)

    def execute(self):
        self.parent.report('This is the default effect')
