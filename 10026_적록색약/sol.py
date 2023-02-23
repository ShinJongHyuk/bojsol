import sys
sys.stdin = open('input.txt')

N = int(input())

arr = [list(map(str,input())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
x, y = 0, 0
visited = [[''] * N for _ in range(N)]
area = []
stack = []
def DFS(x,y):
    global cnt
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        if not visited[x][y]:
            visited[x][y] = arr[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[x][y] == arr[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = arr[x][y]
                stack.append((nx,ny))
    area.append(arr[x][y])
    cnt += 1
    return
cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == '':
            DFS(i,j)
print(cnt, end=' ')
cnt = 0

visited = [[''] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

for i in range(N):
    for j in range(N):
        if visited[i][j] == '':
            DFS(i,j)
print(cnt)


