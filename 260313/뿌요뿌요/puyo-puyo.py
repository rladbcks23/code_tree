n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
boom_group = 0
maximum_blocks = 0
block_cnt = 0
visited = [[False] * n for _ in range(n)]
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

max_num = 0
for i in range(n):
    max_num = max(max_num, max(grid[i]))


def dfs(num, i, j):
    global block_cnt
    for di, dj in delta:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == num and not visited[ni][nj]:
            visited[ni][nj] = True
            block_cnt += 1
            dfs(num, ni, nj)


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            block_cnt = 1
            visited[i][j] = True
            dfs(grid[i][j], i, j)

            maximum_blocks = max(maximum_blocks, block_cnt)
            boom_group += block_cnt//4

print(boom_group, maximum_blocks)
