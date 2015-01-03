import sqlite3


class Database(object):

    def __init__(self, *args):

        if not args:
            self.db = sqlite3.connect(':memory:')
        else:
            self.db = sqlite3.connect(args[0])

    def scrub(self, input_string):
        return ''.join(chr for chr in input_string if chr.isalnum())

    def create_table2(self, name, *args):

        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE ''' + name + '''(id INTEGER PRIMARY KEY)
        ''')

        for i in args:
            cursor.execute(''' ALTER TABLE ''' + name + ''' ADD COLUMN ''' + i)

        self.db.commit()

    def display_table(self, table):

        cursor = self.db.cursor()
        cursor.execute('''
            SELECT * FROM ''' + table)
