n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
group = 0
person = 0
result = []

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]    # 우 하 좌 상
visited = []


def dfs(i, j):
    global person, group
    for di, dj in delta:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1 and (ni, nj) not in visited:
            person += 1
            visited.append((ni, nj))
            dfs(ni, nj)

    return


for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and (i, j) not in visited:
            group += 1
            visited.append((i, j))

            person += 1

            dfs(i, j)

            result.append(person)
            person = 0


print(group)
result.sort()
print('\n'.join(map(str, result)))
