class Pair:
    """Represents the built-in pair data structure in Scheme."""

    def __init__(self, first, rest):
        self.first = first
        self.rest = rest

    def map(self, fn):
        """Maps fn to every element in a list, returning a new
        Pair.
        >>> Pair(1, Pair(2, Pair(3, nil))).map(lambda x: x * x)
        Pair(1, Pair(4, Pair(9, nil)))
        """
        assert isinstance(self.rest, Pair) or self.rest is nil, \
            "rest element in pair must be another pair or nil"
        return Pair(fn(self.first), self.rest.map(fn))

    def __repr__(self):
        return 'Pair({}, {})'.format(self.first, self.rest)


class nil:
    """Represents the special empty pair nil in Scheme."""

    def map(self, fn):
        return nil

    def __getitem__(self, i):
        raise IndexError('Index out of range')

    def __repr__(self):
        return 'nil'


nil = nil()  # this hides the nil class *forever*

# (+ (- 2 4) 6 8)
Pair('+', Pair(Pair('-', Pair(2, Pair(4, nil))), Pair(6, Pair(8, nil))))

