# program to change the position of every n-th value with the (n+1)th in a list.
from itertools import zip_longest, chain, tee
def replace2copy(m):
    m1, m2 = tee(iter(m), 2)
    return list(chain.from_iterable(zip_longest(m[1::2], m[::2])))
n = [7, 9, 8, 5, 6, 4]
print(replace2copy(n))