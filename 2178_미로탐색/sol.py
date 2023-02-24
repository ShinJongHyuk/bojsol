import sys
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(x,y):
    queue = [(x,y)]

    while queue:
        x, y = queue.pop(0)
        if visited[x][y] == 0:
            visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                if nx == N-1 and ny == M-1:
                    return
                queue.append((nx,ny))





N, M = map(int,input().split())
maze = [list(map(int,input())) for _ in range(N)]
queue = []
visited = [[0]*M for _ in range(N)]
BFS(0,0)
print(visited[N-1][M-1])