n, k = map(int, input().split())

lst = list(range(1, n + 1))
result = []

# Please write your code here.
i = 0
while lst:
    for j in range(k):
        i += 1
        if i >= len(lst):
            i = 0
    i -= 1
    result.append(lst.pop(i))

    if i < 0:
        i = 0

print(' '.join(map(str, result)))
