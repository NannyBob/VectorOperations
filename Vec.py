import math


class Vector:

    def __init__(self, *args):
        self.values = args

    def __iter__(self):
        return self.values.__iter__()

    def __len__(self):
        return self.length()

    def __getitem__(self, key):
        return self.values[key]

    def __add__(self, other):
        new_vals = []
        if isinstance(other, Vector):
            biggest = max(len(other.values), len(self.values))
            for i in range(biggest):
                try:
                    a = self[i]
                except IndexError:
                    a = 0
                try:
                    b = other[i]
                except IndexError:
                    b = 0
                new_vals.append(a + b)

        elif isinstance(other, (float, int)):
            new_vals = [a + other for a in self]

        else:
            raise TypeError("Cannot add Vector and " + str(type(other)))

        return Vector(new_vals)

    def __mul__(self, other):
        new_vals = []
        if isinstance(other, (int, float)):
            new_vals = [i * other for i in self]
        return new_vals

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        return self + -other

    def __str__(self):
        return self.values.__str__()

    def dimensions(self):
        return len(self.values)

    @staticmethod
    def scalar_product(x, y) -> float:
        if not x.dimensions() == y.dimensions():
            raise IndexError("Vectors should have the same number of dimensions")
        to_return = 0
        for a, b in zip(x, y):
            to_return += a * b
        return to_return

    def length(self):
        total = 0
        for i in self:
            total += pow(i, 2)
        return math.sqrt(total)

    @staticmethod
    def angle2D(x, y, radians: bool):
        if x.dimensions() < 2 or y.dimensions() < 2:
            raise IndexError("Vectors should have at least 2 dimensions")
        rads = math.acos(Vector.scalar_product(x, y) / x.length() * y.length())
        if radians:
            return rads
        return rads * 180 / math.pi

