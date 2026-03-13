n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = []
delta = [(0, 1), (1, 0)]    # 우, 하
result = 0


def dfs(i, j):
    global result
    if j == m-1 and i == n-1:
        result = 1
        return

    for di, dj in delta:
        ni, nj = i+di, j+dj
        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
            dfs(ni, nj)


dfs(0, 0)

print(result)
