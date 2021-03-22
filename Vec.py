class Vector:

    def __init__(self, *args):
        self.values = args

    def __add__(self, other):
        new_vals = []
        if isinstance(other, Vector):
            new_vals = [a+b for a, b in zip(self.values, other.values)]

        elif isinstance(other, (float, int)):
            new_vals = [a + other for a in self.values]

        return new_vals
