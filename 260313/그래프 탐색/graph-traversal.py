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


def dfs(depth, num):
    global result
    if depth == n:
        return
    can_move = False
    if num in tree.keys():
        for t in tree[num] and t not in visited:
            can_move = True
            visited.append(t)
            dfs(depth + 1, t)
            visited.pop()

    if not can_move:
        result = max(result, depth)
        return


dfs(0, 1)

print(result)
