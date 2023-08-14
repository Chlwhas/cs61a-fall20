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
            return f'Link({self.first})'
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


def flip_two(lnk):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    if lnk is not Link.empty and lnk.rest is not Link.empty:
        value_1 = lnk.first
        value_2 = lnk.rest.first
        lnk.first = value_2
        lnk.rest.first = value_1
        flip_two(lnk.rest.rest)

    # while link is not Link.empty:
    #     if f(link.first):
    #         yield link.first
    #     link = link.rest


def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> next(g)
    4
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """

    if link is not Link.empty:
        if f(link.first):
            yield link.first

        if link.rest is not Link.empty:
            for e in filter_link(link.rest, f):
                yield e


class Tree:

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches


def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """

    if t.label % 2 != 0:
        t.label += 1
    if not t.is_leaf():
        for branch in t.branches:
            make_even(branch)

def square_tree(t):
    """Mutates a Tree t by squaring all its elements.
    >>> t2 = Tree(2, [Tree(3, [Tree(4)]), Tree(5)])
    >>> square_tree(t2)
    >>> t2.label
    4
    >>> t2.branches[0].label
    9
    >>> t2.branches[0].branches[0].label
    16
    >>> t2.branches[1].label
    25
    """
    t.label = t.label ** 2
    if not t.is_leaf():
        for branch in t.branches:
            square_tree(branch)


def find_paths(t, entry):
    """
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    """
    # 如果树是空的，直接返回空列表
    if not t:
        return []

    # 如果找到entry，返回包含当前标签的路径
    if t.label == entry:
        return [[t.label]]

    paths = []

    # 对于每一个子树，查找从子树到entry的所有路径
    for branch in t.branches:
        for subpath in find_paths(branch, entry):
            # 合并当前的标签和子路径，然后添加到结果中
            paths.append([t.label] + subpath)

    return paths


def combine_tree(t1, t2, combiner):
    """
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    if t1.is_leaf() and t2.is_leaf():
        return Tree(combiner(t1.label, t2.label))
    branches = []
    for (branch1, branch2) in zip(t1.branches, t2.branches):
        branches.append(combine_tree(branch1, branch2, combiner))
    return Tree(combiner(t1.label, t2.label), branches)


def alt_tree_map(t, map_fn):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> alt_tree_map(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    """

    if t.is_leaf():
        return Tree(map_fn(t.label))

    for branch in t.branches:
        for sub_branch in branch.branches:
            sub_branch.label = map_fn(sub_branch.label)

