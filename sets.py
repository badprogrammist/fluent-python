def set_hashing_example():
    try:
        s = {set(['1, 2', '3'])}
    except TypeError:
        pass

    s = {frozenset(['1', '2', '3'])}


def set_operations():
    assert {1, 2, 3} | {2, 3, 4} == {1, 2, 3, 4}
    assert {1, 2, 3}.union({2, 3, 4}) == {1, 2, 3, 4}
    assert {1, 2, 3}.union([2, 3, 4]) == {1, 2, 3, 4}
    assert {1, 2, 3}.union((2, 3, 4)) == {1, 2, 3, 4}
    assert {1, 2, 3}.union({2, 3, 4}, [5, 6], (7, 8)) == {1, 2, 3, 4, 5, 6, 7, 8}

    assert {1, 2, 3} & {2, 3, 4} == {2, 3}
    assert {1, 2, 3}.intersection({2, 3, 4}) == {2, 3}
    assert {1, 2, 3}.intersection([2, 3, 4]) == {2, 3}
    assert {1, 2, 3}.intersection((2, 3, 4)) == {2, 3}
    assert {1, 2, 3}.intersection({2, 3, 4}, [5, 2, 3], (2, 3, 8)) == {2, 3}

    assert {1, 2, 3} - {2, 3, 4} == {1}
    assert {1, 2, 3}.difference({2, 3, 4}) == {1}
    assert {1, 2, 3}.difference([2, 3, 4]) == {1}
    assert {1, 2, 3}.difference((2, 3, 4)) == {1}
    assert {1, 2, 3, 5}.difference({2, 3, 4}, [1, 6]) == {5}
    assert {2, 3, 4} - {1, 2, 3} == {4}
    assert {2, 3, 4}.difference({1, 2, 3}) == {4}
    assert {2, 3, 4}.difference({1, 2, 3}, (4, 5)) == set() # {} - is a dict

    assert {1, 2, 3} ^ {2, 3, 4} == {1, 4}
    assert {2, 3, 4} ^ {1, 2, 3} == {1, 4}
    assert {1, 2, 3}.symmetric_difference({2, 3, 4}) == {1, 4}

def set_predicates():
    assert {2, 3} <= {1, 2, 3}
    assert {2, 3}.issubset({1, 2, 3})
    assert {2, 3}.issubset([1, 2, 3])
    assert {2, 3}.issubset((1, 2, 3))
    assert {1, 2, 3} <= {1, 2, 3}

    assert {2, 3} < {1, 2, 3}
    assert ({1, 2, 3} < {1, 2, 3}) is False

    assert {1, 2, 3} > {1, 2}
    assert {1, 2, 3}.issuperset({1, 2})
    assert {1, 2, 3}.issuperset([1, 2])
    assert {1, 2, 3}.issuperset((1, 2))
    assert ({1, 2} > {1, 2, 3}) is False

def set_comps():
    s = {str(i) for i in range(0, 10) if i % 2 == 0}
    assert s == {'0', '2', '4', '6', '8'}

def set_data_operations():
    s = {1, 2}

    s.add(3)
    assert s == {1, 2, 3}

    s.discard(4)
    assert s == {1, 2, 3}
    s.discard(1)
    assert s == {2, 3}

    assert s.pop() == 2
    assert s == {3}

    try:
        s.remove(5)
    except KeyError:
        pass
    s.remove(3)
    assert s == set()

    try:
        s.pop()
    except KeyError:
        pass


if __name__ == '__main__':
    set_hashing_example()
    set_operations()
    set_comps()
    set_predicates()
    set_data_operations()
