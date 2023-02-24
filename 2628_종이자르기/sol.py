import sys
sys.stdin = open('input.txt')

N, M = map(int,input().split())

paper = [[0]*N for _ in range(M)]

T = int(input())
row = [0,N]
col = [0,M]
for _ in range(T):
    x, y = map(int,input().split())
    if x == 0:
        col.append(y)
    else:
        row.append(y)
row.sort()
col.sort()
x = 0
y = 0
for i in range(len(row) - 1):
    if row[i+1] - row[i] > x:
        x = row[i+1] - row[i]
for i in range(len(col) - 1):
    if col[i+1] - col[i] > y:
        y = col[i+1] - col[i]
print(x*y)



