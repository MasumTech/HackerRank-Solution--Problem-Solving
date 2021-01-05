# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

A = set(list(map(int, input().strip().split()))[:n])
A = set(A)
# print(A)

n = int(input())
for i in range(n):
    op, x = map(str, input().split())
    x = int(x)
    # print(op)
    # print(x)
    B = list(map(int, input().strip().split()))[:x]
    B = set(B)
    # print(B)

    if op == 'intersection_update':
        A.intersection_update(B)
        # print(A)

    elif op == 'update':
        A.update(B)
        # print(A)

    elif op == 'symmetric_difference_update':
        A.symmetric_difference_update(B)
        # print(A)

    elif op == 'difference_update':
        A.difference_update(B)
        # print(A)

print(sum(A))


