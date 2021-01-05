import numpy

n, m = map(int, input().split())
A = []
for i in range(n):
    a = [int(x) for x in input().split()]
    A.append(a)

A1 = (numpy.sum(A, axis=0))

# print(A1)

sum = 1
for x in A1:
    sum = sum * x

print(sum)