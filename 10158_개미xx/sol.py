import sys
sys.stdin = open('input.txt')

w, h = map(int,input().split())
x, y = map(int,input().split())
T = int(input())

dx = 1
dy = 1

for i in range(T):
    nx = x + dx
    ny = y + dy
    if nx == w and 0 < ny < h:
        dx = -1
    elif 0 < nx < w and ny == h:
        dy = -1
    elif nx == 0 and 0 < ny < h:
        dx = 1
    elif 0 < nx < w and ny == 0:
        dy = 1
    elif nx == w and ny == h:
        dx,dy = -1, -1
    elif nx == 0 and ny == 0:
        dx, dy = 1, 1
    x = nx
    y = ny
print(x,y)
