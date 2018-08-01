import array
import collections
import bisect
import random

symbols = '$¢£'
colors = ['black', 'white']
sizes = ['S', 'M', 'L']


def using_listcomps():
    codes = [ord(symbol) for symbol in symbols]
    assert codes == [36, 162, 163]


def listcomps_vs_map_filter():
    codes = [ord(symbol) for symbol in symbols if ord(symbol) > 161]
    assert codes == [162, 163]

    codes = list(filter(lambda c: c > 161, map(ord, symbols)))
    assert codes == [162, 163]


def the_cartesian_production_by_listcomps():
    tshirts = [(color, size) for color in colors
               for size in sizes]
    assert len(tshirts) == 6


def using_genexps():
    codes_tuple = tuple(ord(symbol) for symbol in symbols)
    assert codes_tuple == (36, 162, 163)

    codes_array = array.array('I', (ord(symbol) for symbol in symbols))
    assert codes_array.tolist() == [36, 162, 163]


def the_cartesian_production_by_genexps():
    for tshirt in ((color, size) for color in colors
                   for size in sizes):
        print(tshirt)


def tuples_as_records():
    traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567')]

    for passport in sorted(traveler_ids):
        print('%s/%s' % passport)

    for country, _ in traveler_ids:
        print(country)


def tuple_unpacking():
    city, year, pop = ('Tokyo', 2003, 32450)
    assert city == 'Tokyo'
    assert year == 2003
    assert pop == 32450

    lax_coordinates = (33.94, -118.41)
    latitude, longitude = lax_coordinates
    assert latitude == 33.94
    assert longitude == -118.41

    a, b = (5, 4)
    b, a = a, b
    assert a == 4
    assert b == 5

    assert divmod(20, 8) == (2, 4)
    t = (20, 8)
    assert divmod(*t) == (2, 4)


def grab_excess_items():
    a, b, *rest = range(5)
    assert a == 0
    assert b == 1
    assert rest == [2, 3, 4]

    a, b, *body, c = range(5)
    assert a == 0
    assert b == 1
    assert body == [2, 3]
    assert c == 4


def nested_tuple_unpacking():
    metro_areas = [('Tokyo', (35.68, 139.69)),
                   ('Sao Paulo', (-23.55, -46.64)),
                   ('Mexico City', (19.43, -99.13))]
    print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
    fmt = '{:15} | {:9.2f} | {:9.2f}'

    for name, (latitude, longitude) in metro_areas:
        print(fmt.format(name, latitude, longitude))


def named_tuples():
    City = collections.namedtuple('City', ['name', 'coordinates'])

    tokyo = City('Tokyo', (35.68, 139.69))
    assert tokyo.name == 'Tokyo'
    assert tokyo.coordinates == (35.68, 139.69)
    assert tokyo._fields == ('name', 'coordinates')

    LatLong = collections.namedtuple('LatLong', ['lat', 'long'])

    tokyo_data = City('Tokyo', LatLong(35.68, 139.69))
    tokyo1 = City._make(tokyo_data)
    assert tokyo1.name == 'Tokyo'
    assert tokyo1.coordinates == (35.68, 139.69)

    tokyo2 = City(*tokyo_data)
    assert tokyo2.name == 'Tokyo'
    assert tokyo2.coordinates == (35.68, 139.69)


def slicing():
    s = '1234567'
    assert s[::2] == '1357'
    assert s[::-1] == '7654321'
    assert s[::-2] == '7531'
    assert s[0:4:2] == '13'
    slc = slice(0, 4, 2)
    assert s[slc] == '13'


def assigning_to_slices():
    l = list(range(10))

    l[2:5] = [20, 30]
    assert l == [0, 1, 20, 30, 5, 6, 7, 8, 9]

    del l[5:7]
    assert l == [0, 1, 20, 30, 5, 8, 9]

    l[3::2] = [11, 22]
    assert l == [0, 1, 20, 11, 5, 22, 9]

    l[2:5] = [100]
    assert l == [0, 1, 100, 22, 9]


def building_list_of_lists():
    board = [['_'] * 3 for _ in range(3)]
    assert board == [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    board[1][2] = 'X'
    assert board == [['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]

    board = [['_'] * 3] * 3
    assert board == [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    board[1][2] = 'O'
    assert board == [['_', '_', 'O'], ['_', '_', 'O'], ['_', '_', 'O']]


def augmented_assignment():
    l = [1, 2, 3]
    x = id(l)
    l *= 2
    assert l == [1, 2, 3, 1, 2, 3] and id(l) == x

    t = (1, 2, 3)
    x = id(t)
    t *= 2
    assert t == (1, 2, 3, 1, 2, 3) and id(t) != x


def assignment_puzzler():
    t = (1, 2, [30, 40])  # bad idea
    try:
        t[2] += [50, 60]  # trying to change immutable object
    except TypeError:
        pass
    assert t == (1, 2, [30, 40, 50, 60])  # the operation is not atomic: we got the error and changed the state


def sorting():
    fruits = ['grape', 'raspberry', 'apple', 'banana']

    assert sorted(fruits) == ['apple', 'banana', 'grape', 'raspberry']
    assert sorted(fruits, key=len, reverse=True) == ['raspberry', 'banana', 'grape',
                                                     'apple']  # the sorting algorithm is stable: grape and apple have the same order as the original sequence
    assert fruits == ['grape', 'raspberry', 'apple', 'banana']  # original sequence is not changed

    fruits.sort()
    assert fruits == ['apple', 'banana', 'grape', 'raspberry']


def using_bisect():
    def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
        i = bisect.bisect_right(breakpoints, score)
        return grades[i]

    assert grade(33) == 'F'
    assert grade(99) == 'A'
    assert grade(77) == 'C'
    assert grade(70) == 'C'
    assert grade(89) == 'B'
    assert grade(90) == 'A'
    assert grade(100) == 'A'


def keep_the_seq_sorted():
    l = []
    bisect.insort(l, 5)
    bisect.insort(l, 3)
    assert l == [3, 5]
    bisect.insort(l, 2)
    assert l == [2, 3, 5]
    bisect.insort(l, 8)
    assert l == [2, 3, 5, 8]

def using_array():
    floats = array.array('d', (random.random() for _ in range(1000)))
    f = floats[-1]

    fp = open('floats.bin', 'wb')
    floats.tofile(fp)
    fp.close()

    floats2 = array.array('d')

    fp = open('floats.bin', 'rb')
    floats2.fromfile(fp, 1000)
    fp.close()

    assert floats2[-1] == f
    assert floats == floats2

def array_sorting():
    a = array.array('I', [5, 4, 3, 2, 1])
    s = array.array(a.typecode, sorted(a))
    assert s.tolist() == [1, 2, 3, 4, 5]


def using_deque():
    dq = collections.deque([1, 2, 3, 4, 5], maxlen=10)
    dq.rotate(2)
    assert dq == collections.deque([4, 5, 1, 2, 3], maxlen=10)
    dq.rotate(-3)
    assert dq == collections.deque([2, 3,4, 5, 1], maxlen=10)
    dq.appendleft(-1)
    assert dq == collections.deque([-1, 2, 3, 4, 5, 1], maxlen=10)
    dq.extend([6, 7])
    assert dq == collections.deque([-1, 2, 3, 4, 5, 1, 6, 7], maxlen=10)
    dq.extendleft([-2, -3])
    assert dq == collections.deque([-3, -2, -1, 2, 3, 4, 5, 1, 6, 7], maxlen=10)

if __name__ == '__main__':
    using_listcomps()
    listcomps_vs_map_filter()
    the_cartesian_production_by_listcomps()
    using_genexps()
    the_cartesian_production_by_genexps()
    tuples_as_records()
    tuple_unpacking()
    grab_excess_items()
    nested_tuple_unpacking()
    named_tuples()
    slicing()
    assigning_to_slices()
    building_list_of_lists()
    augmented_assignment()
    assignment_puzzler()
    sorting()
    using_bisect()
    keep_the_seq_sorted()
    using_array()
    array_sorting()
    using_deque()
