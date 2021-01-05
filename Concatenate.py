import numpy

n, m, o = map(int, input().split())
A = []
B = []

for i in range(n):
    a = [int(x) for x in input().split()]
    A.append(a)

for i in range(m):
    b = [int(x) for x in input().split()]
    B.append(b)

# print(A)
# print(B)

print(numpy.concatenate((A, B), axis=0))