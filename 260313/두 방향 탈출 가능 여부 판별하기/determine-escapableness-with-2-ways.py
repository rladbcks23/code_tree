n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = []
delta = [(0, 1), (1, 0)]    # 우, 하


def dfs(i, j):
    if j == n-1 and i == n-1:
        return 1

    for di, dj in delta:
        ni, nj = i+di, j+dj
        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
            return dfs(ni, nj)
    return 0


result = dfs(0, 0)
print(result)
