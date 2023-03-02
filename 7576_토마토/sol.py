import sys
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(x,y,cnt):
    queue = [(x,y)]
    while queue:
        x, y = queue.pop(0)
        if visited[cnt][x][y] == 0:
            visited[cnt][x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and (arr[nx][ny] == 0 or 1) and visited[cnt][nx][ny] == 0:
                visited[cnt][nx][ny] = visited[cnt][x][y] + 1
                queue.append((nx,ny))
    return

M, N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
queue = []
loca = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            loca.append([i,j])
visited = [[[0]*M for _ in range(N)] for _ in range(len(loca))]
for k in range(len(loca)):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == -1:
                visited[k][i][j] = -1
cnt = 0
for i in loca:
    x, y = i[0], i[1]
    BFS(x,y,cnt)
    cnt += 1

for i in visited:
    for j in i:
        print(j)
    print()

result = []


