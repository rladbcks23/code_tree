n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

delta = [(0, 1), (1, 0)]
result = 0
visited = [[False] * m for _ in range(n)]

def dfs(i, j):
    global result
    if result:          # 이미 찾았으면 바로 종료
        return
    if i == n-1 and j == m-1:
        result = 1
        return

    for di, dj in delta:
        ni, nj = i+di, j+dj
        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1 and not visited[ni][nj]:
            visited[ni][nj] = True
            dfs(ni, nj)

visited[0][0] = True
dfs(0, 0)
print(result)