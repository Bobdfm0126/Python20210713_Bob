# __init__
# __call__

class Foo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return 'Foo (%d, %d)' % (self.x, self.y)


class Bar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return 'Bar (%d, %d)' % (self.x, self.y)


