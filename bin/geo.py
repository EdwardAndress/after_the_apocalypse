import numpy


class Geometric(object):

    def __init__(self):
        pass

    def is_index(self, index_list):

        try:
            length = len(index_list)
        except:
            print('Supplied argument ', index_list, ' does not return a length')
            return False

        if length != 2:
            print('Supplied argument ', index_list, ' is not two items long')
            return False

        return True

    def get_distance(self, point_a, point_b):
        valid_a = self.is_index(point_a)
        valid_b = self.is_index(point_b)

        if valid_a and valid_b:

            x_distance = valid_a[0] - valid_b[0]
            y_distance = valid_a[1] - valid_b[1]

            return self.hypotenuse(x_distance, y_distance)

    def hypotenuse(self, a, b):
        return (a * a + b * b)**.5


class Grid(Geometric):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = self.generate_grid(self.width, self.height)

        self.centre_x = int(width/2)
        self.centre_y = int(width/2)

    def __setitem__(self, key, value):
        pass

    def __getitem__(self, item):
        pass

    def set(self, x, y, value):

        abs_x, abs_y = self.relative_to_absolute(x, y)

        self.grid[abs_x][abs_y] = value

    def get(self, x, y):

        abs_x, abs_y = self.relative_to_absolute(x, y)

        return self.grid[abs_x][abs_y]

    def generate_grid(self, width, height):

        columns = [None] * width

        i = 0

        while i < height:

            #print(i)
            #print(height)

            columns[i] = [None] * height
            i += 1

        return columns

    def relative_to_absolute(self, x, y):

        if x < 0:
            absolute_x = self.centre_x - abs(x)

        else:
            absolute_x = self.width - self.centre_x + x

        if y < 0:
            absolute_y = self.centre_y - abs(y)

        else:
            absolute_y = self.height - self.centre_y + y

        return absolute_x, absolute_y


class Path(Geometric):

    def __init__(self, start, end, *points):
        pass


