import sys
sys.stdin = open('input.txt')
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(x,y):
    global cnt
    queue = [(x,y)]
    while queue:
        x, y = queue.pop(0)
        cnt += 1
        if visited[x][y] == 0:
            visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny))
    return
N, M, K = map(int,input().split())
arr = [[0]*M for _ in range(N)]
queue = []
result = []
cnt = 0
visited = [[0]*M for _ in range(N)]
for _ in range(K):
    r, c = map(int,input().split())
    arr[r-1][c-1] = 1
for x in range(N):
    for y in range(M):
        if arr[x][y] == 1:
            cnt = 0
            BFS(x,y)
            result.append(cnt)
print(max(result))
