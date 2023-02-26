import sys
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(x,y):
    visited = [[0]*(ay+1) for _ in range(ax+1)]
    queue = [(x,y)]
    while queue:
        x, y = queue.pop(0)
        if visited[x][y] == 0:
            visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= ax and 0 <= ny <= ay and not visited[nx][ny] and arr[nx][ny]:
                if arr[nx][ny] == 3:
                    return visited[x][y]
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    return 0


queue = []
ay, ax = map(int,input().split())
arr = [[0]*(ay+1) for _ in range(ax+1)]
for i in range(ax):
    arr[i][0] = 1
    arr[i][ay] = 1
for j in range(ay+1):
    arr[0][j] = 1
    arr[ax][j] = 1
N = int(input())
position = []
for i in range(N):
    a, b = map(int,input().split()) # 1 = 북 / 2 = 남 / 3= 서 / 4 = 동
    if a == 1:
        arr[0][b] = 2
    elif a == 2:
        arr[ax][b] = 2
    elif a == 3:
        arr[b][0] = 2
    elif a == 4:
        arr[b][ay] = 2

da, db = map(int, input().split())
if da == 1:
    arr[0][db] = 3
elif da == 2:
    arr[ax][db] = 3
elif da == 3:
    arr[db][0] = 3
elif da == 4:
    arr[db][ay] = 3

result = 0
for i in range(ax+1):
    for j in range(ay+1):
        if arr[i][j] == 2:
            result += BFS(i,j)
print(result)