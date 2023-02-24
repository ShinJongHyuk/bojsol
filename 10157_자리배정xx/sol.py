import sys
sys.stdin = open('input.txt')

C, R = map(int,input().split()) # C = 가로, R = 세로
K = int(input()) # K = 관객 수

arr = [[0]*R for _ in range(C)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dir = 0

cnt = 1
x, y = C, 0
arr[x][y] = 1

while C*R < 0 :
    nx =
