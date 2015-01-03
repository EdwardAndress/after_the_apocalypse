__author__ = 'jimnarey'

class Converter(object):

    def __init__(self, name, table):
        self.name = name
        self.table = table
        pass


# Could load from a database or, failing that, load from a hardcoded dictionary
gutter = {

    'animal' : ['hide', 'meat'],
    'fish' : ['fish_oil', 'fish_meat']

}