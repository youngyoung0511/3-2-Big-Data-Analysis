#20221333 김서영
#Assignment 1-1

import numpy as np

a = np.zeros(3, dtype=[('a', 'f4'), ('b', 'i4'), ('c', 'S5')])
b = np.zeros(3, dtype=[('a', 'f2'), ('b', 'i2'), ('c', 'S2')])

a_expanded = np.array([(0.5, 2, b'a'), (1., 4, b'aa'), (1.5, 6, b'aaa'), (2., 8, b'aaaa'), (2.5, 10, b'aaaaa'), (3., 12, b'aaaaa'),(3.5, 14, b'aaaaa'), (4., 16, b'aaaaaa'), (4.5, 18, b'aaaaaaa'), (5., 20, b'aaaaaaa'), (5.5, 22, b'aaaaaaa'), (6., 24, b'aaaaaaa'),  (6.5, 26, b'aaaaaaa')], dtype=[('a', 'f4'), ('b', 'i4'), ('c', 'S7')])
b_expanded = np.array([(1., 1, b'a'), (4., 32, b'b'), (9., 243, b'c'), (16., 1024, b'd'), (25., 3125, b'e'), (36., 7776, b'f'),(49., 16807, b'g'), (64., -32768, b'h'), (81., -6487, b'i'), (100., -31072, b'j')], dtype=[('a', 'f2'), ('b', 'i2'), ('c', 'S2')])
a = np.concatenate([a_expanded[:3], a_expanded[3:]])
b = np.concatenate([b_expanded[:3], b_expanded[3:]])

print(a)
print(b)
