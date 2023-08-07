from operator import mul


class A:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return self.x

    def __str__(self):
        return self.x * 2


class B:
    def __init__(self):
        print("boo!")
        self.a = []

    def add_a(self, a):
        self.a.append(a)

    def __repr__(self):
        print(len(self.a))
        ret = ''
        for a in self.a:
            ret += str(a)
        return ret


class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty:
            return f'Link{self.first}'
        else:
            return f'Link({self.first}, {repr(self.rest)})'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

    def __len__(self):
        if self is Link.empty:
            return 0
        else:
            return 1 + len(self.rest)


def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if lnk is Link.empty:
        return 0
    else:
        return lnk.first + sum_nums(lnk.rest)


def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    result_len = min([len(lnk) for lnk in lst_of_lnks])
    list_value = []

    for _ in range(result_len):
        value = 1
        for lnk in lst_of_lnks:
            value *= lnk.first
        list_value.append(value)

        for i in range(len(lst_of_lnks)):
            lst_of_lnks[i] = lst_of_lnks[i].rest

    def list_to_link(lst):
        if len(lst) == 1:
            return Link(lst[0])
        else:
            return Link(lst[0], list_to_link(lst[1:]))

    return list_to_link(list_value)

