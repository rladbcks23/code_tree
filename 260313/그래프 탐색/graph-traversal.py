n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
from collections import defaultdict

tree = defaultdict(list)

for k, d in edges:
    tree[k].append(d)
    tree[d].append(k)

result = 0
visited = [1]


def dfs(num):
    global result

    for t in tree[num]:
        if t not in visited:
            result += 1
            visited.append(t)
            dfs(t)


dfs(1)

print(result)
