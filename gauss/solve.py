'''
Jason loves listening to J-pop. YouTube Music reported his total listening time (in minutes) in the past year.
Jason said the time is the inner product of the shortest basis vectors of the lattice with basis {(114, 2024), (514, 1012)}.
Can you figure out the time?
'''

from sage.all import vector, matrix, ZZ
from Crypto.Util.number import long_to_bytes

c = vector(ZZ, [114, 2024])
d = vector(ZZ, [514, 1012])


def gauss(v1, v2):
    while True:
        if v2.norm() < v1.norm():
            v1, v2 = v2, v1
        m = round(v1*v2/(v1*v1))
        if m == 0:
            return v1, v2
        v2 = v2-m*v1

a, b = gauss(c, d)


#a, b = matrix([c, d]).LLL() # shortest_basis_vectors = lattice.LLL()
print('a = ', a)
print('b = ', b)
print('a*b = ', a*b)
