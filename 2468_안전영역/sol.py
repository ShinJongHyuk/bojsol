import sys
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(x,y):
    global cnt
    cnt += 1
    q = [(x,y)]

    while q:
        x, y = q.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                visited[nx][ny] = 2
                q.append((nx,ny))

    return
N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]


result = []
maxv = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] > maxv:
            maxv = arr[i][j]

for k in range(1,maxv+1):
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] < k:
                visited[i][j] = 1
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                BFS(i,j)
    result.append(cnt)
print(max(result))
