import sys
sys.stdin = open('input.txt')

arr = [list(map(int,input().split())) for _ in range(19)]

dx = [-1, 0, 1, 1]
dy = [1, 1, 1, 0]

for x in range(19):
    for y in range(19):
        if arr[x][y] == 1 or arr[x][y] == 2:
            for i in range(4):
                cnt = 0
                for j in range(1,5):
                    nx = x + dx[i] * j
                    ny = y + dy[i] * j
                    if 0 <= nx < 19 and 0 <= ny < 19 and arr[x][y] == arr[nx][ny]:
                        cnt += 1
                if cnt == 4:
                    if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and 0 <= x + dx[i]*5 < 19 and 0 <= y + dy[i]*5 < 19:
                        if arr[x - dx[i]][y - dy[i]] != arr[x][y] and arr[x + dx[i] * 5][y + dy[i] * 5] != arr[x][y]:
                            print(arr[x][y])
                            print(x+1,y+1)
                            exit()
                    elif 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and (x + dx[i]*5 > 18 or y + dy[i]*5 > 18):
                        if arr[x - dx[i]][y - dy[i]] != arr[x][y]:
                            print(arr[x][y])
                            print(x + 1, y + 1)
                            exit()
                    elif 0 <= x + dx[i]*5 < 19 and 0 <= y + dy[i]*5 < 19 and (y - dy[i] < 0 or x - dx[i] < 0):
                        if arr[x + dx[i] * 5][y + dy[i] * 5] != arr[x][y]:
                            print(arr[x][y])
                            print(x + 1, y + 1)
                            exit()
                    else:
                        print(arr[x][y])
                        print(x + 1, y + 1)
                        exit()
print(0)
