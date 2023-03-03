import sys
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(x,y):
    visited = [[0] * M for _ in range(N)]
    q = [(x,y)]

    while q:
        x, y = q.pop(0)
        if visited[x][y] == 0:
            visited[x][y] = 1
        if x == N-1 and y == M-1:
            return visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
    return -1

N, M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
q = []
result = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            arr[i][j] = 0
            result.append(BFS(0,0))
            arr[i][j] = 1

print(max(result))

