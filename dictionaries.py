import collections.abc
import types


def dict_ancestry():
    assert isinstance({}, collections.abc.Mapping)


def hashable_elements():
    assert hash((1, 2, (30, 40))) is not None

    try:
        hash((1, 2, [30, 40]))  # list is not hashable
    except TypeError:
        pass

    assert hash((1, 2, frozenset([30, 40]))) is not None

    class NotEqualType:
        def __init__(self, prop):
            self.prop = prop

    assert NotEqualType('1') != NotEqualType('1')
    not_equal_obj = NotEqualType('1')
    assert hash(not_equal_obj) != id(not_equal_obj)

    class EqualType:
        def __init__(self, prop):
            self.prop = prop

        def __eq__(self, other):
            return self.prop == other.prop

        def __hash__(self):
            return hash(self.prop)

    assert EqualType('1') == EqualType('1')
    assert hash(EqualType('1')) == hash(EqualType('1'))
    equal_obj = EqualType('1')
    assert hash(equal_obj) != id(equal_obj)


def various_ways_to_build_dict():
    a = dict(one=1, two=2, three=3)
    b = {'one': 1, 'two': 2, 'three': 3}
    c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    d = dict([('two', 2), ('one', 1), ('three', 3)])
    e = dict({'three': 3, 'one': 1, 'two': 2})

    assert a == b == c == d == e


def dict_comprehensions():
    DIAL_CODES = [(7, 'Russia'),
                  (1, 'USA'),
                  (91, 'India')]
    d = {country: code for code, country in DIAL_CODES}
    assert d == {'Russia': 7, 'USA': 1, 'India': 91}

    du = {country.upper(): code for code, country in DIAL_CODES}
    assert du == {'RUSSIA': 7, 'USA': 1, 'INDIA': 91}


def setdefault_example():
    d = {'1': [1, 2], '3': [5, 6]}
    d.setdefault('2', [3]).append(4)
    assert d == {'1': [1, 2], '2': [3, 4], '3': [5, 6]}

    d2 = {'1': [1, 2], '2': [3], '3': [5, 6]}
    d2.setdefault('2', [3]).append(4)
    assert d2 == {'1': [1, 2], '2': [3, 4], '3': [5, 6]}


def defaultdict_example():
    dd = collections.defaultdict(list)
    assert dd.get('2') is None
    assert isinstance(dd['2'], list)
    assert dd.get('2') is not None
    dd['2'].append(2)
    assert dd['2'] == [2]


def missing_method_example():
    # The best practice is not to inherit from dict class.
    # Use collections.UserDict instead

    class StrKeyDict(dict):
        def __missing__(self, key):
            if isinstance(key, str):
                raise KeyError(key)
            return self[str(key)]

        def get(self, key, default=None):
            try:
                return self[key]
            except KeyError:
                return default

        def __contains__(self, key):
            return (key in self.keys()
                    or str(key) in self.keys())

    d = StrKeyDict([('2', 'two'), ('4', 'four')])

    assert d['2'] == 'two'
    assert d[2] == 'two'
    assert d.get('4') == 'four'
    assert d.get(3) is None
    assert d.get(3, 'n/a') == 'n/a'
    assert 2 in d
    assert '4' in d
    assert '3' not in d
    assert 3 not in d


def chain_map_example():
    cm = collections.ChainMap(
        {'a': 1, 'b': 2},
        {'a': 3, 'c': 4})
    assert cm['a'] == 1
    assert cm['b'] == 2
    assert cm['c'] == 4

    cm = cm.new_child({'a': 5, 'c': 6})
    assert cm['a'] == 5
    assert cm['b'] == 2
    assert cm['c'] == 6

    cm = cm.parents
    assert cm['a'] == 1
    assert cm['b'] == 2
    assert cm['c'] == 4


def counter_example():
    c = collections.Counter('abracadabra')
    assert c['a'] == 5
    assert c['b'] == 2

    c.update('aabbbb')
    assert c['a'] == 7
    assert c['b'] == 6

    most_common = c.most_common(2)
    assert most_common[0] == ('a', 7)
    assert most_common[1] == ('b', 6)


def user_dict_example():
    class StrKeyDict(collections.UserDict):
        def __missing__(self, key):
            if isinstance(key, str):
                raise KeyError(key)
            return self[str(key)]

        def __contains__(self, key):
            return str(key) in self.data

        def __setitem__(self, key, value):
            self.data[str(key)] = value

    d = StrKeyDict([('2', 'two'), ('4', 'four')])

    assert d['2'] == 'two'
    assert d[2] == 'two'
    assert d.get('4') == 'four'
    assert d.get(3) is None
    assert d.get(3, 'n/a') == 'n/a'
    assert 2 in d
    assert '4' in d
    assert '3' not in d
    assert 3 not in d


def mapping_proxy_type_example():
    d = {'a': 1, 'b': 2}
    proxy = types.MappingProxyType(d)

    assert proxy['a'] == 1
    assert proxy['b'] == 2

    try:
        proxy['a'] = 3
    except TypeError:
        pass

    d['a'] = 3
    assert proxy['a'] == 3
    d['c'] = 4
    assert proxy['c'] == 4


if __name__ == '__main__':
    set_hashing_example()
    set_operations()
