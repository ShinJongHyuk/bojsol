import sys
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x,y):
    global cnt
    stack = [(x,y)]

    while stack:
        x, y = stack.pop()
        if visited[x][y] == 0:
            visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny]:
                visited[nx][ny] = 1
                stack.append((nx,ny))
    cnt += 1
    return

T = int(input())

for tc in range(1,T+1):
    N, M, K = map(int,input().split()) # N = x좌표 M = y좌표 K= 배추의 개수
    arr = [[0]*M for _ in range(N)]
    visited = [[0]*M for i_ in range(N)]
    stack = []
    cnt = 0
    for _ in range(K):
        x, y = map(int,input().split())
        arr[x][y] = 1

    for x in range(N):
        for y in range(M):
            if arr[x][y] and not visited[x][y]:
                DFS(x,y)
    print(cnt)