import numpy

n = int(input())
A = []
B = []

for i in range(n):  # A for loop for row entries
    a = []
    a = [int(x) for x in input().split()]
    A.append(a)

for i in range(n):  # A for loop for row entries
    b = []
    b = [int(x) for x in input().split()]
    B.append(b)

A = numpy.array(A)
B = numpy.array(B)

print(numpy.dot(A, B))