import numpy

n, m = map(int, input().split())
A = []
A1 = []
for i in range(n):
    a = []
    a = [int(x) for x in input().split()]
    A.append(a)

print(max(numpy.min(A, axis=1)))




