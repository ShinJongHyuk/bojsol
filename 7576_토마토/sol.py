import sys
sys.stdin = open('input.txt')
from collections import deque

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
# def BFS(x,y,cnt):
#     queue = [(x,y)]
#     while queue:
#         x, y = queue.pop(0)
#         if visited[cnt][x][y] == 0:
#             visited[cnt][x][y] = 1
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < N and 0 <= ny < M and (arr[nx][ny] == 0 or 1) and visited[cnt][nx][ny] == 0:
#                 visited[cnt][nx][ny] = visited[cnt][x][y] + 1
#                 queue.append((nx,ny))
#     return
#
# M, N = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(N)]
# queue = []
# loca = []
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 1:
#             loca.append([i,j])
# visited = [[[0]*M for _ in range(N)] for _ in range(len(loca))]
# for k in range(len(loca)):
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == -1:
#                 visited[k][i][j] = -1
# cnt = 0
# for i in loca:
#     x, y = i[0], i[1]
#     BFS(x,y,cnt)
#     cnt += 1
#
# for i in range(len(loca)):

##########################################

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
# def BFS(A: list):
#     queue = A
#     while queue:
#         for _ in range(len(A)):
#             x, y = queue.pop(0)
#             if visited[x][y] == 0:
#                 visited[x][y] = 1
#             for j in range(4):
#                 nx = x + dx[j]
#                 ny = y + dy[j]
#                 if 0 <= nx < N and 0 <= ny < M and (arr[nx][ny] == 0 or 1) and visited[nx][ny] == 0:
#                     visited[nx][ny] = visited[x][y] + 1
#                     queue.append((nx,ny))
#     return
#
# M, N = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(N)]
#
# loca = []
#
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 1:
#             loca.append((i,j))
#
# visited = [[0]*M for _ in range(N)]
# for k in range(len(loca)):
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == -1:
#                 visited[i][j] = -1
#
# BFS(loca)
# result = 0
# for i in range(N):
#     for j in range(M):
#         if visited[i][j] > result:
#             result = visited[i][j]
# for i in visited:
#     if 0 in i:
#         print(-1)
#         break
# else:
#     print(result-1)
###################
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
# def BFS(A: list):
#     queue = A
#     while queue:
#         x, y = queue.pop(0)
#         for j in range(4):
#             nx = x + dx[j]
#             ny = y + dy[j]
#             if 0 > nx or nx >= N or 0 > ny or ny >= M:
#                 continue
#             else:
#                 if arr[nx][ny] == 0:
#                     arr[nx][ny] = arr[x][y] + 1
#                     queue.append((nx,ny))
#     return
#
# M, N = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(N)]
#
# loca = []
#
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 1:
#             loca.append((i,j))
# BFS(loca)
# result = 0
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] > result:
#             result = arr[i][j]
# for i in arr:
#     if 0 in i:
#         print(-1)
#         break
# else:
#     print(result-1)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

M, N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
queue = deque([])

def BFS():
    while queue:
        x,y = queue.popleft()
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 > nx or nx >= N or 0 > ny or ny >= M:
                continue
            else:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1
                    queue.append([nx,ny])
    return

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append([i,j])
BFS()
result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] > result:
            result = arr[i][j]
for i in arr:
    if 0 in i:
        print(-1)
        break
else:
    print(result-1)

