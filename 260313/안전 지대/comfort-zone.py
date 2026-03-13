n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
group = 0
result = []

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]    # 우 하 좌 상


def dfs(i, j, k):
    for di, dj in delta:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] > k and (ni, nj) not in visited:
            visited.append((ni, nj))
            dfs(ni, nj, k)


max_num = 0
for i in range(n):
    max_num = max(max_num, max(grid[i]))


for k in range(1, max_num):
    visited = []
    group = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] > k and (i, j) not in visited:
                visited.append((i, j))
                group += 1
                dfs(i, j, k)
    result.append((group, k))

max_group = 0
for i in range(len(result)):
    max_group = max(max_group, result[i][0])

for i in range(len(result)):
    if result[i][0] < max_group:
        result[i] = (100, 100)

result.sort()

if not result:
    result.append((1, 0))

print(' '.join(map(str, result[0])))
