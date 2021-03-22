class Vector:

    def __init__(self, *args):
        self.values = args

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
        new_vals =[]
        if isinstance(other, (int, float)):
            new_vals = [i * other for i in self]

    def __divmod__(self, other):

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        return self + -other

    def __str__(self):
        return self.values.__str__()