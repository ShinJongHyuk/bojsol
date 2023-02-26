import sys
sys.stdin = open('input.txt')

C, R = map(int,input().split()) # C = 가로, R = 세로 인데 C = 세로 R = 가로 로 할 예정
K = int(input()) # K = 관객 수

arr = [[0]*(R+1) for _ in range(C+1)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = 0

cnt = 1
x, y = 1,1
arr[x][y] = 1

while cnt < C*R:
    nx = x + dx[dir]
    ny = y + dy[dir]

    if 1 <= nx <= C and 1 <= ny <= R and arr[nx][ny] == 0:
        cnt += 1
        arr[nx][ny] = cnt
        x, y = nx, ny
    else:
        dir += 1
        if dir >= 4:
            dir = 0
result = []
for i in range(C+1):
    for j in range(R+1):
        if arr[i][j] == K:
            result.append(str(i))
            result.append(str(j))
if result:
    print(' '.join(result))
else:
    print(0)
